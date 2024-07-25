#include <iostream>
#include <valarray>
#include <algorithm>
#include <numeric>

template <class element_type>
class matrix {
public:
    matrix(size_t width, size_t height): m_stride(width), m_height(height), m_storage(width*height) {  }

    element_type &operator()(size_t row, size_t column)
    {
        // column major
        return m_storage[std::slice(column, m_height, m_stride)][row];

        // row major
        return m_storage[std::slice(row, m_stride, m_height)][column];
    }

private:
    std::valarray<element_type> m_storage;
    size_t m_stride;
    size_t m_height;
};


int main() {
  std::valarray<double> v0(100);
  std::iota(std::begin(v0), std::end(v0), 0);
  std::for_each(std::begin(v0), std::end(v0), [](auto& v) {std::cout << v << std::endl; });
  std::cout << "========\n";

  std::valarray<double> v1 = v0[std::slice(3, 10, 10)];
  std::for_each(std::begin(v1), std::end(v1), [](auto& v) {std::cout << v << std::endl; });

  std::cout << "end" << std::endl;
  return 0;
}
