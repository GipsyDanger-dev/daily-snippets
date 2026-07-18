# C++ Templates untuk Generic Programming

**Kategori:** C++ for ML | **Difficulty:** Intermediate | **Session:** Afternoon | **Date:** 2026-07-18

---


## Apa itu Templates?

Templates memungkinkan menulis **kode generic** yang bekerja dengan tipe data apapun. Ini adalah fondasi dari **generic programming** di C++.

## Function Templates

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

// Template function
template <typename T>
T find_max(T a, T b) {
    return (a > b) ? a : b;
}

// Template dengan multiple type parameters
template <typename T, typename U>
auto add(T a, U b) -> decltype(a + b) {
    return a + b;
}

int main() {
    std::cout << find_max(3, 5) << std::endl;        // int
    std::cout << find_max(3.14, 2.71) << std::endl;  // double
    std::cout << find_max('a', 'z') << std::endl;    // char

    auto result = add(3, 2.14);  // int + double = double
    std::cout << result << std::endl;

    return 0;
}
```

## Class Templates

```cpp
template <typename T>
class Stack {
private:
    std::vector<T> elements;

public:
    void push(const T& elem) {
        elements.push_back(elem);
    }

    T pop() {
        T elem = elements.back();
        elements.pop_back();
        return elem;
    }

    T top() const {
        return elements.back();
    }

    bool empty() const {
        return elements.empty();
    }

    size_t size() const {
        return elements.size();
    }
};

int main() {
    Stack<int> intStack;
    intStack.push(1);
    intStack.push(2);
    std::cout << intStack.pop() << std::endl;  // 2

    Stack<std::string> strStack;
    strStack.push("Hello");
    strStack.push("World");
    std::cout << strStack.pop() << std::endl;  // World

    return 0;
}
```

## Template Specialization

```cpp
template <typename T>
class Printer {
public:
    void print(T value) {
        std::cout << "Value: " << value << std::endl;
    }
};

// Specialization for bool
template <>
class Printer<bool> {
public:
    void print(bool value) {
        std::cout << "Boolean: " << (value ? "true" : "false") << std::endl;
    }
};

// Specialization for pointer types
template <typename T>
class Printer<T*> {
public:
    void print(T* value) {
        std::cout << "Pointer to: " << *value << std::endl;
    }
};

int main() {
    Printer<int> intPrinter;
    intPrinter.print(42);  // Value: 42

    Printer<bool> boolPrinter;
    boolPrinter.print(true);  // Boolean: true

    int x = 10;
    Printer<int*> ptrPrinter;
    ptrPrinter.print(&x);  // Pointer to: 10

    return 0;
}
```

## Variadic Templates

```cpp
// Base case
void print() {}

// Variadic template
template <typename T, typename... Args>
void print(T first, Args... rest) {
    std::cout << first;
    if constexpr (sizeof...(rest) > 0) {
        std::cout << ", ";
        print(rest...);
    }
}

// Fold expression (C++17)
template <typename... Args>
auto sum(Args... args) {
    return (args + ...);
}

int main() {
    print(1, "hello", 3.14, 'x');  // 1, hello, 3.14, x

    std::cout << sum(1, 2, 3, 4, 5) << std::endl;  // 15

    return 0;
}
```

## Template Metaprogramming

```cpp
// Compile-time factorial
template <int N>
struct Factorial {
    static constexpr int value = N * Factorial<N-1>::value;
};

template <>
struct Factorial<0> {
    static constexpr int value = 1;
};

// Compile-time fibonacci
template <int N>
struct Fibonacci {
    static constexpr int value = Fibonacci<N-1>::value + Fibonacci<N-2>::value;
};

template <>
struct Fibonacci<0> { static constexpr int value = 0; };
template <>
struct Fibonacci<1> { static constexpr int value = 1; };

int main() {
    // Computed at compile time!
    std::cout << "5! = " << Factorial<5>::value << std::endl;  // 120
    std::cout << "Fib(10) = " << Fibonacci<10>::value << std::endl;  // 55

    return 0;
}
```

## SFINAE and Concepts (C++20)

```cpp
// SFINAE (Substitution Failure Is Not An Error)
template <typename T>
typename std::enable_if<std::is_arithmetic<T>::value, T>::type
safe_divide(T a, T b) {
    return b != 0 ? a / b : 0;
}

// C++20 Concepts (cleaner syntax)
template <typename T>
concept Numeric = std::is_arithmetic_v<T>;

template <Numeric T>
T safe_add(T a, T b) {
    return a + b;
}

int main() {
    std::cout << safe_divide(10, 3) << std::endl;
    std::cout << safe_add(1.5, 2.5) << std::endl;
    // safe_add("hello", "world");  // Error! Not Numeric
    return 0;
}
```

## Latihan

1. Implement generic Matrix class using templates
2. Create a type-safe heterogeneous container
3. Write a compile-time string concatenation
4. Implement a simple variant type using templates

## Sumber Belajar

- [C++ Templates: The Complete Guide](https://www.amazon.com/C-Templates-Complete-Guide-2nd/dp/0321714127)
- [cppreference Templates](https://en.cppreference.com/w/cpp/language/templates)
