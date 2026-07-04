#include <iostream>
#include <fstream>
#include <ctime>

void log_event(const std::string& message) {
    std::ofstream log("security.log", std::ios_base::app);
    std::time_t now = std::time(0);
    log << std::ctime(&now) << ": " << message << std::endl;
}
