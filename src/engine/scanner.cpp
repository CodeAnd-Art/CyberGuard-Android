#include <iostream>
#include <filesystem>
#include <string>

namespace fs = std::filesystem;

bool is_suspicious(const std::string& path) {
    // 50KB'dan küçük dosyaları şüpheli işaretle
    if (fs::exists(path) && fs::file_size(path) < 51200) {
        return true;
    }
    return false;
}

int main(int argc, char* argv[]) {
    if (argc < 2) return 1;
    if (is_suspicious(argv[1])) {
        std::cout << "THREAT_DETECTED" << std::endl;
    } else {
        std::cout << "CLEAN" << std::endl;
    }
    return 0;
}
