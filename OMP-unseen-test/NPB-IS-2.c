   #pragma omp for nowait schedule(static)
    for( i=0; i<NUM_KEYS; i++ )
        work_buff[key_buff_ptr2[i]]++;
