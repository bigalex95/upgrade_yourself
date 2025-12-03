#pragma once
#include <iostream>
#include <memory>
#include <vector>
#include <string>

// Эмуляция OpenCV (для примера, если нет библиотеки под рукой)
struct Mat
{
    int width, height;
    std::vector<uint8_t> data;

    Mat(int w, int h) : width(w), height(h), data(w * h, 0)
    {
        std::cout << "  [Mat] Memory allocated: " << w * h << " bytes" << std::endl;
    }

    // Деструктор покажет нам, когда память очистится
    ~Mat()
    {
        std::cout << "  [Mat] Memory freed" << std::endl;
    }
};

class CameraDriver
{
public:
    CameraDriver() { std::cout << "Camera Initialized.\n"; }
    ~CameraDriver() { std::cout << "Camera Closed.\n"; }

    // Функция возвращает unique_ptr.
    // Это значит: "Я отдаю тебе этот кадр, теперь ты за него отвечаешь".
    std::unique_ptr<Mat> captureFrame()
    {
        // make_unique - самый безопасный способ создания (C++14)
        return std::make_unique<Mat>(1920, 1080);
    }
};

// ПЛОХОЙ ПРИМЕР (на интервью так не пиши):
// void processBad(Mat image) { ... } // Вызовет полное копирование данных!

// ХОРОШИЙ ПРИМЕР:
// const & (константная ссылка) - мы только читаем, копирования нет.
void processFrame(const Mat &image)
{
    std::cout << "Processing frame of size " << image.width << "x" << image.height << "...\n";
    // Тут какая-то логика CV...
}

void run_smart_pointers_and_efficiency()
{
    // 1. Создаем драйвер. unique_ptr гарантирует, что камера закроется при выходе.
    auto camera = std::make_unique<CameraDriver>();

    std::cout << "--- Loop Start ---\n";

    // 2. Захватываем кадр
    // framePtr владеет данными кадра
    std::unique_ptr<Mat> framePtr = camera->captureFrame();

    if (framePtr)
    {
        // 3. Передаем по ссылке (разыменовываем указатель *framePtr)
        processFrame(*framePtr);
    }

    std::cout << "--- Loop End ---\n";

    // Здесь framePtr выйдет из области видимости и память Mat очистится сама.
    // Затем удалится camera.
    return;
}