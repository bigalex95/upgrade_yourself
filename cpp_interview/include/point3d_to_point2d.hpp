#pragma once
#include <iostream>
#include <vector>

// Простая структура для 3D точки (например, от Лидара)
struct Point3D
{
    float x, y, z;
};

// Простая структура для 2D точки (пиксель)
struct Point2D
{
    int u, v;
};

// Параметры камеры (Intrinsics)
struct CameraIntrinsics
{
    float fx, fy; // Фокусное расстояние (в пикселях)
    float cx, cy; // Оптический центр (обычно w/2, h/2)
};

// Функция проецирования
// В реальности R и T - это матрицы, здесь упростим для понимания логики
Point2D projectLidarToImage(const Point3D &pointLidar,
                            const CameraIntrinsics &cam,
                            const float rotationMatrix[3][3],
                            const float translationVector[3])
{

    // 1. Трансформация из системы Лидара в систему Камеры (Extrinsics)
    // P_cam = R * P_lidar + T
    float x_cam = rotationMatrix[0][0] * pointLidar.x + rotationMatrix[0][1] * pointLidar.y + rotationMatrix[0][2] * pointLidar.z + translationVector[0];
    float y_cam = rotationMatrix[1][0] * pointLidar.x + rotationMatrix[1][1] * pointLidar.y + rotationMatrix[1][2] * pointLidar.z + translationVector[1];
    float z_cam = rotationMatrix[2][0] * pointLidar.x + rotationMatrix[2][1] * pointLidar.y + rotationMatrix[2][2] * pointLidar.z + translationVector[2];

    // ВАЖНАЯ ПРОВЕРКА: Точка должна быть ПЕРЕД камерой (Z > 0)
    if (z_cam <= 0)
    {
        // Точка сзади камеры, её нельзя отобразить
        return {-1, -1};
    }

    // 2. Проекция на плоскость изображения (Perspective Divide)
    // Мы делим на глубину Z, чтобы получить перспективу (далекие объекты меньше)
    float u_normalized = x_cam / z_cam;
    float v_normalized = y_cam / z_cam;

    // 3. Перевод в пиксели (Intrinsics)
    Point2D pixel;
    pixel.u = static_cast<int>(cam.fx * u_normalized + cam.cx);
    pixel.v = static_cast<int>(cam.fy * v_normalized + cam.cy);

    return pixel;
}

void run_point3d_to_point2d()
{
    // Пример: Камера смотрит прямо, Лидар стоит в той же точке (единичная матрица R, нулевой T)
    CameraIntrinsics K = {1000.0f, 1000.0f, 640.0f, 360.0f};

    // Точка на 10 метров впереди, 2 метра правее
    Point3D lidarPoint = {2.0f, 0.0f, 10.0f};

    // Упрощенные R (единичная) и T (нули) для примера
    float R[3][3] = {{1, 0, 0}, {0, 1, 0}, {0, 0, 1}};
    float T[3] = {0, 0, 0};

    Point2D uv = projectLidarToImage(lidarPoint, K, R, T);

    std::cout << "Pixel coordinates: U=" << uv.u << ", V=" << uv.v << std::endl;
    // Ожидаем:
    // u = 1000 * (2/10) + 640 = 200 + 640 = 840
    // v = 1000 * (0/10) + 360 = 360

    return;
}