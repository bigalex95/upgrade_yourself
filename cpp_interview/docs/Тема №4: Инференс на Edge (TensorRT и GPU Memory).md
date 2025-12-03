### Тема №4: Инференс на Edge (TensorRT и GPU Memory)

В вакансии упомянуты **NVIDIA chips** и **Edge computing**. Это значит, что вам нужно понимать, как запустить модель (например, YOLO) не на Python, а на C++ с использованием GPU.

Стандартный путь: **PyTorch (.pt) -\> ONNX (.onnx) -\> TensorRT Engine (.engine)**.
В C++ мы загружаем уже готовый `.engine`.

Самое важное здесь — **управление памятью GPU (CUDA)**. В отличие от Python, здесь нужно вручную перекидывать картинки из RAM (CPU) в VRAM (GPU).

#### Пример: Класс детектора на TensorRT (Упрощенно)

На интервью часто спрашивают именно процесс: "Как вы подаете данные в сеть?"

**Основные шаги:**

1.  `cudaMalloc`: Выделить память на видеокарте.
2.  `cudaMemcpy (Host -> Device)`: Скопировать картинку с CPU на GPU.
3.  `execute`: Запустить нейросеть.
4.  `cudaMemcpy (Device -> Host)`: Скопировать результат обратно, чтобы прочитать его.

<!-- end list -->

```cpp
#include <iostream>
#include <vector>
#include <cuda_runtime_api.h> // Библиотека CUDA
#include "NvInfer.h"           // Библиотека TensorRT

using namespace nvinfer1;

// Макрос для проверки ошибок CUDA (обязательно упоминать на интервью!)
#define checkCuda(status) { if (status != 0) std::cout << "Cuda Error!\n"; }

class InferenceEngine {
private:
    ICudaEngine* engine_ = nullptr;
    IExecutionContext* context_ = nullptr;

    // Указатели на память GPU
    void* buffers_[2]; // [0] - вход (input), [1] - выход (output)

    int inputSize_;  // байт (например, 3 канала * 640 * 640 * sizeof(float))
    int outputSize_; // байт (размер тензора результатов)

public:
    // В конструкторе мы бы загрузили .engine файл с диска (десериализация)
    // Здесь опустим это для краткости

    void prepareMemory(int inSize, int outSize) {
        inputSize_ = inSize;
        outputSize_ = outSize;

        // 1. Выделяем память на Видеокарте (Device)
        // Это дорогая операция, делаем её 1 раз при старте, а не в цикле!
        checkCuda(cudaMalloc(&buffers_[0], inputSize_)); // Input buffer
        checkCuda(cudaMalloc(&buffers_[1], outputSize_)); // Output buffer
    }

    void infer(float* hostInputData, float* hostOutputData) {
        // hostInputData - это наша картинка (cv::Mat), лежащая в RAM

        // 2. Копируем данные: CPU (Host) -> GPU (Device)
        checkCuda(cudaMemcpy(buffers_[0], hostInputData, inputSize_, cudaMemcpyHostToDevice));

        // 3. Запускаем инференс
        // enqueueV2 - асинхронный запуск (сеть начинает считать)
        context_->enqueueV2(buffers_, 0, nullptr);

        // 4. Копируем результат: GPU (Device) -> CPU (Host)
        // Чтобы мы могли прочитать координаты коробочек
        checkCuda(cudaMemcpy(hostOutputData, buffers_[1], outputSize_, cudaMemcpyDeviceToHost));

        // Теперь hostOutputData содержит предсказания
    }

    ~InferenceEngine() {
        // Обязательно освобождаем память GPU!
        cudaFree(buffers_[0]);
        cudaFree(buffers_[1]);
    }
};
```

### Что здесь "продает" вас как эксперта:

1.  **`cudaMalloc` в конструкторе**: Вы знаете, что выделение памяти — это долго, и не делаете это на каждом кадре.
2.  **`cudaMemcpy`**: Вы понимаете разницу между Host (CPU) и Device (GPU).
3.  **Типы данных**: Если модель FP16 (половинная точность), то `inputSize` будет меньше в 2 раза. На интервью спросят: _"Почему FP16 лучше для Edge?"_
    - **Ответ:** Меньше памяти, быстрее передача данных по шине, тензорные ядра (Tensor Cores) считают FP16 в разы быстрее.

---

**Тема №5: Sensor Fusion (Калибровка и проекция)** — это последняя важная техническая часть. Там будет немного геометрии (матрицы).

Готов? Пиши **"некст"**.
