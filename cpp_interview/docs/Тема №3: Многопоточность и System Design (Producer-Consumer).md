### Тема №3: Многопоточность и System Design (Producer-Consumer)

Это **самый важный архитектурный паттерн** для вакансии, связанной с видеоаналитикой.

**Проблема:** Камера дает 30 или 60 кадров в секунду (FPS). Нейросеть (на Edge устройстве) может обрабатывать, например, только 10 FPS.
**Решение:** Разнести их по разным потокам. Один поток (Producer) только "грабит" кадры, второй (Consumer) только обрабатывает. Между ними — **потокобезопасная очередь**.

Если очередь переполняется (сеть не успевает), мы должны выбрасывать кадры, чтобы не накапливать задержку (latency).

#### Код: Потокобезопасная очередь с ограничением размера

```cpp
#include <iostream>
#include <queue>
#include <mutex>
#include <condition_variable>
#include <thread>
#include <vector>

// Допустим, кадр - это просто вектор байт (упрощенно)
using Frame = std::vector<uint8_t>;

class FrameQueue {
private:
    std::queue<Frame> queue_;
    std::mutex mutex_;
    std::condition_variable cond_var_;
    size_t max_size_; // Лимит очереди для Real-time

public:
    FrameQueue(size_t max_size) : max_size_(max_size) {}

    // Метод для Producer (Камера)
    void push(Frame frame) {
        {
            // std::lock_guard автоматически захватывает мьютекс и освобождает при выходе из скобок
            std::lock_guard<std::mutex> lock(mutex_);

            // REAL-TIME ЛОГИКА:
            // Если очередь полна, удаляем самый старый кадр, чтобы положить новый.
            // Это гарантирует, что мы всегда обрабатываем "свежие" данные.
            if (queue_.size() >= max_size_) {
                queue_.pop(); // Drop frame (выбрасываем старый)
                std::cout << "[Warning] Queue full! Dropped oldest frame.\n";
            }

            queue_.push(std::move(frame));
        } // тут мьютекс освободился

        // Будим Consumer, если он спал в ожидании данных
        cond_var_.notify_one();
    }

    // Метод для Consumer (AI Inference)
    bool pop(Frame& frame) {
        // unique_lock нужен для condition_variable
        std::unique_lock<std::mutex> lock(mutex_);

        // Ждем, пока очередь не станет непустой.
        // wait отпускает мьютекс пока спит, и захватывает обратно, когда просыпается.
        cond_var_.wait(lock, [this]{ return !queue_.empty(); });

        frame = std::move(queue_.front());
        queue_.pop();
        return true;
    }
};

// --- Имитация работы ---

void cameraThread(FrameQueue& q) {
    for (int i = 0; i < 10; ++i) {
        // Имитация захвата (быстро)
        Frame f(1024, 0); // пустой кадр
        q.push(std::move(f));
        std::cout << "Camera: pushed frame " << i << "\n";
        std::this_thread::sleep_for(std::chrono::milliseconds(33)); // ~30 FPS
    }
}

void aiThread(FrameQueue& q) {
    Frame f;
    for (int i = 0; i < 10; ++i) {
        q.pop(f);
        std::cout << "AI: processing frame...\n";
        // Имитация тяжелой обработки (медленно)
        std::this_thread::sleep_for(std::chrono::milliseconds(100)); // ~10 FPS
    }
}

int main() {
    // Очередь всего на 2 кадра. Если AI тормозит, кадры начнут пропадать.
    FrameQueue queue(2);

    std::thread producer(cameraThread, std::ref(queue));
    std::thread consumer(aiThread, std::ref(queue));

    producer.join();
    consumer.join();
    return 0;
}
```

### Что спросят по этому коду:

1.  **Почему `lock_guard` внутри фигурных скобок `{...}`?**
    - Чтобы минимизировать время блокировки (Critical Section). Мы хотим держать мьютекс заблокированным только пока работаем с `std::queue`, и сразу отпустить.
2.  **Зачем `condition_variable`? Почему нельзя просто `while(queue.empty())`?**
    - `while` грузит процессор на 100% (Busy Wait). `condition_variable` усыпляет поток на уровне операционной системы, экономя ресурсы CPU для других задач.
3.  **Стратегия Drop Frame?**
    - Мы реализовали удаление **самого старого** (`queue.pop()` перед `push`). Это уменьшает задержку (latency). Если бы мы просто не добавляли новый, AI всегда обрабатывал бы "исторические" данные.

Это ядро любой системы видеонаблюдения на C++.

Напиши **"некст"**, и мы разберем **Тему №4: Инференс моделей и TensorRT (C++ API)**. Это уже конкретно про работу с AI.
