### Тема №6: Калибровка камеры (Camera Calibration)

Это базовый вопрос для Computer Vision. Если вы работаете с лидарами, SLAM или просто хотите измерять расстояния по видео, вам нужна **откалиброванная камера**.

**Суть:**
Обычная камера искажает картинку (линзы округляют края — "рыбий глаз"). Калибровка позволяет найти математическую модель (матрицы), чтобы выпрямить изображение и соотнести пиксели с реальным миром.

**Что мы ищем (Output):**

1.  **Intrinsics (Внутренние параметры):** Матрица $K$. Содержит фокусное расстояние ($f_x, f_y$) и оптический центр ($c_x, c_y$).
2.  **Distortion Coefficients (Дисторсия):** Вектор коэффициентов ($k_1, k_2, p_1, p_2...$), описывающий искривление линзы.

---

### Алгоритм ("Шахматная доска")

Стандартный метод — использование шахматной доски (Chessboard).

1.  Берем доску с известным размером клетки (например, 30 мм).
2.  Делаем 10-20 фото с разных углов.
3.  Находим углы клеток на фото (2D точки).
4.  Сопоставляем их с реальной сеткой (3D точки, где $Z=0$).
5.  Решаем уравнение минимизации ошибки (**Reprojection Error**).

### Код на C++ (OpenCV)

Вот пример того, как это выглядит в коде. На интервью важно упомянуть `findChessboardCorners` и `calibrateCamera`.

```cpp
#include <opencv2/opencv.hpp>
#include <vector>
#include <iostream>

void calibrateMyCamera() {
    // 1. Подготовка "идеальных" 3D точек (Object Points)
    // Мы знаем, как выглядит доска в реальности: (0,0,0), (1,0,0), (2,0,0)...
    int boardWidth = 9;  // кол-во внутренних углов по ширине
    int boardHeight = 6; // кол-во внутренних углов по высоте
    float squareSize = 0.025f; // 25 мм размер клетки (в метрах)

    std::vector<cv::Point3f> objp;
    for(int i = 0; i < boardHeight; i++) {
        for(int j = 0; j < boardWidth; j++) {
            objp.push_back(cv::Point3f(j * squareSize, i * squareSize, 0));
        }
    }

    // Контейнеры для всех снимков
    std::vector<std::vector<cv::Point3f>> objectPoints; // 3D точки
    std::vector<std::vector<cv::Point2f>> imagePoints;  // 2D точки на картинке

    // 2. Цикл по изображениям (представим, что у нас есть список файлов)
    std::vector<cv::String> images;
    cv::glob("calibration_imgs/*.jpg", images);

    cv::Mat frame, gray;
    for(const auto& file : images) {
        frame = cv::imread(file);
        cv::cvtColor(frame, gray, cv::COLOR_BGR2GRAY);

        std::vector<cv::Point2f> corners;

        // Ищем углы шахматной доски
        bool found = cv::findChessboardCorners(gray, cv::Size(boardWidth, boardHeight), corners);

        if(found) {
            // ВАЖНО ДЛЯ ИНТЕРВЬЮ: Sub-pixel Refinement
            // Уточняем координаты углов с точностью до долей пикселя. Это повышает точность в разы.
            cv::cornerSubPix(gray, corners, cv::Size(11, 11), cv::Size(-1, -1),
                cv::TermCriteria(cv::TermCriteria::EPS + cv::TermCriteria::COUNT, 30, 0.1));

            imagePoints.push_back(corners);
            objectPoints.push_back(objp);
        }
    }

    // 3. Запуск калибровки
    cv::Mat cameraMatrix, distCoeffs; // Результаты (Intrinsics и Дисторсия)
    std::vector<cv::Mat> R, T;        // Extrinsics для каждого снимка (нам они обычно не нужны)

    double reprojectionError = cv::calibrateCamera(objectPoints, imagePoints, gray.size(),
                                                   cameraMatrix, distCoeffs, R, T);

    std::cout << "Calibration done with Reprojection Error: " << reprojectionError << std::endl;
    std::cout << "Camera Matrix (K):\n" << cameraMatrix << std::endl;
    std::cout << "Distortion Coeffs:\n" << distCoeffs << std::endl;
}
```

### Возможные вопросы на интервью:

1.  **Что такое ошибка репроекции (Reprojection Error)?**

    - **Ответ:** Это среднее расстояние (в пикселях) между тем, где угол был найден на фото, и тем, куда он "спроецировался" математически с использованием найденных параметров. Хороший результат — **меньше 0.5 - 1.0 пикселя**.

2.  **Зачем нужен `cornerSubPix`?**

    - **Ответ:** Функция `findChessboardCorners` дает просто координаты пикселя (целые числа). `cornerSubPix` использует градиенты, чтобы найти точный угол (например, 10.45, 20.12). Без этого точная калибровка для Edge/Military задач невозможна.

3.  **В чем разница между Radial и Tangential distortion?**

    - **Radial:** Линза искривляет прямые линии в дуги ("бочка" или "подушка").
    - **Tangential:** Линза установлена не идеально параллельно сенсору (кривая сборка).
