#pragma omp simd
            for ( c = c_start; c < c_start + BLOCK_SIZE_C; ++c ) {
                result[r*col+c] =temp[r*col+c]+
                     ( Cap_1 * (power[r*col+c] +
                    (temp[(r+1)*col+c] + temp[(r-1)*col+c] - 2.f*temp[r*col+c]) * Ry_1 +
                    (temp[r*col+c+1] + temp[r*col+c-1] - 2.f*temp[r*col+c]) * Rx_1 +
                    (amb_temp - temp[r*col+c]) * Rz_1));
            }
