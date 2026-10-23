// C++20 geographic-distance kernel, called from Python through ctypes.
#include <algorithm>
#include <cmath>
#include <numbers>
extern "C" {
void haversine_batch(const double* lat, const double* lon, int n,
                     double lat0, double lon0, double* out_km) {
    constexpr double R = 6371.0088, rad = std::numbers::pi / 180.0;
    const double p0 = lat0 * rad;
    for (int i = 0; i < n; ++i) {
        const double p1 = lat[i] * rad, dp = p1 - p0, dl = (lon[i] - lon0) * rad;
        const double a = std::sin(dp / 2) * std::sin(dp / 2) +
                         std::cos(p0) * std::cos(p1) * std::sin(dl / 2) * std::sin(dl / 2);
        out_km[i] = 2 * R * std::asin(std::sqrt(std::min(1.0, a)));
    }
}
}
