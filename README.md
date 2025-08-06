# LinearInterpolation_CB

This project demonstrates a circular buffer implementation with linear interpolation for variable fractional delay, commonly used in digital audio effects and real-time DSP systems.

<br>

## Overview

A circular buffer (also called a ring buffer) is a fixed-size buffer that wraps around once it reaches the end. It is highly efficient for implementing delay lines in real-time audio applications, avoiding the costly memory shift operations of linear buffers.

In this implementation, we combine a circular buffer with **fractional delay capability** using **linear interpolation**.

<br>

## Features

- **Power-of-2 buffer size** with bitmask wraparound for performance optimization
- **Fixed delay** using a read pointer
- **Overrun/Underrun protection** via 1-slot empty rule
- **Floating-point read/write pointers** for sub-sample accuracy
- **Linear interpolation** between buffer samples

<br>

## Circular Buffer Logic

We use two separate pointers:

- `write_pointer`: Where new samples are written  
- `read_pointer`: Where delayed/interpolated samples are read

To ensure safe real-time operation:

- **Write** is **disallowed** when `next_write == read_pointer` (Overrun)
- **Read** is **disallowed** when `read_pointer == write_pointer` (Underrun)

This design follows the **1-slot empty rule**, which simplifies detection of full and empty conditions while preventing data loss.

<br>

## Linear Interpolation

To achieve fractional delay (non-integer sample delay), we implement linear interpolation:

Given a floating-point read pointer `r`:

```python
low = int(r)
high = (low + 1) % buffer_size
a = r - low

interpolated_value = (1 - a) * buffer[low] + a * buffer[high]
```

This allows sub-sample resolution delay, which is essential for applications like flanging, chorus, pitch shifting, or physical modeling.

<br>

## Files

- `LinearInterpolation_CB.py`: Core implementation
- `README.md`: Project documentation

