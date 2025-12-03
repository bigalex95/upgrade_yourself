#pragma once
#include <iostream>
#include <queue>
#include <mutex>
#include <condition_variable>
#include <thread>
#include <vector>

// Допустим, кадр - это просто вектор байт (упрощенно)
using Frame = std::vector<uint8_t>;

class FrameQueue
{
private:
    std::queue<Frame> queue_;
    std::mutex mutex_;
    std::condition_variable cond_var_;
    size_t max_size_;      // Лимит очереди для Real-time
    bool stopped_ = false; // Флаг завершения

public:
    FrameQueue(size_t max_size) : max_size_(max_size) {}

    // Метод для Producer (Камера)
    void push(Frame frame)
    {
        {
            std::lock_guard<std::mutex> lock(mutex_);
            if (queue_.size() >= max_size_)
            {
                queue_.pop();
                std::cout << "[Warning] Queue full! Dropped oldest frame.\n";
            }
            queue_.push(std::move(frame));
        }
        cond_var_.notify_one();
    }

    // Метод для Consumer (AI Inference)
    bool pop(Frame &frame)
    {
        std::unique_lock<std::mutex> lock(mutex_);
        cond_var_.wait(lock, [this]
                       { return !queue_.empty() || stopped_; });
        if (queue_.empty())
            return false; // Если очередь пуста и остановлено
        frame = std::move(queue_.front());
        queue_.pop();
        return true;
    }

    // Метод для сигнала остановки
    void stop()
    {
        {
            std::lock_guard<std::mutex> lock(mutex_);
            stopped_ = true;
        }
        cond_var_.notify_all();
    }
};

// --- Имитация работы ---

void cameraThread(FrameQueue &q)
{
    for (int i = 0; i < 10; ++i)
    {
        Frame f(1024, 0);
        q.push(std::move(f));
        std::cout << "Camera: pushed frame " << i << "\n";
        std::this_thread::sleep_for(std::chrono::milliseconds(33));
    }
    q.stop(); // Сигнализируем о завершении
}

void aiThread(FrameQueue &q)
{
    Frame f;
    while (q.pop(f))
    {
        std::cout << "AI: processing frame...\n";
        std::this_thread::sleep_for(std::chrono::milliseconds(100));
    }
    std::cout << "AI: stopped, no more frames.\n";
}

void run_producer_consumer()
{
    FrameQueue queue(2);

    std::thread producer(cameraThread, std::ref(queue));
    std::thread consumer(aiThread, std::ref(queue));

    producer.join();
    consumer.join();
    return;
}