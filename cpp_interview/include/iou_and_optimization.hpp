#pragma once
#include <iostream>
#include <algorithm> // для std::max, std::min

struct BBox
{
    float x1, y1, x2, y2; // Левый-верхний и правый-нижний углы

    float area() const
    {
        // +1 часто добавляют в пиксельных координатах,
        // но в нормализованных (0.0-1.0) или float координатах обычно просто разница
        return (x2 - x1) * (y2 - y1);
    }
};

float calculateIoU(const BBox &boxA, const BBox &boxB)
{
    // 1. Находим координаты прямоугольника пересечения
    // Для левого верхнего угла берем MAX, для правого нижнего MIN
    float xA = std::max(boxA.x1, boxB.x1);
    float yA = std::max(boxA.y1, boxB.y1);
    float xB = std::min(boxA.x2, boxB.x2);
    float yB = std::min(boxA.y2, boxB.y2);

    // 2. Вычисляем ширину и высоту пересечения
    // Если прямоугольники не пересекаются, разница будет отрицательной, поэтому ставим 0
    float interWidth = std::max(0.0f, xB - xA);
    float interHeight = std::max(0.0f, yB - yA);

    float interArea = interWidth * interHeight;

    // Если пересечения нет, сразу возвращаем 0, чтобы не делить
    if (interArea == 0.0f)
        return 0.0f;

    // 3. Вычисляем Union
    float boxAArea = boxA.area();
    float boxBArea = boxB.area();

    float unionArea = boxAArea + boxBArea - interArea;

    // 4. Результат
    return interArea / unionArea;
}

void run_iou_and_optimization()
{
    // Пример: два сильно перекрывающихся бокса
    BBox gt = {100, 100, 200, 200};   // Ground Truth (100x100)
    BBox pred = {110, 110, 210, 210}; // Prediction (смещен на 10px)

    std::cout << "IoU: " << calculateIoU(gt, pred) << std::endl;

    return;
}