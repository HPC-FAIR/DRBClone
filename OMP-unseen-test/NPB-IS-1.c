    #pragma omp parallel for private(i,j,k,k1) schedule(dynamic)
    for( j=0; j< NUM_BUCKETS; j++ ) {

        k1 = (j > 0)? bucket_ptrs[j-1] : 0;
        for ( i = k1; i < bucket_ptrs[j]; i++ ) {
            k = --key_buff_ptr_global[key_buff2[i]];
            key_array[k] = key_buff2[i];
        }
    }
