#include <iostream>
#include "smart_pointers_and_efficiency.hpp"
#include "iou_and_optimization.hpp"
#include "producer_consumer.hpp"
#include "point3d_to_point2d.hpp"

int main()
{
    run_smart_pointers_and_efficiency();
    std::cout << "***************************************" << std::endl;
    run_iou_and_optimization();
    std::cout << "***************************************" << std::endl;
    run_producer_consumer();
    std::cout << "***************************************" << std::endl;
    run_point3d_to_point2d();
    std::cout << "***************************************" << std::endl;

    return 0;
}