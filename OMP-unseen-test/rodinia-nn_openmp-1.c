        #pragma omp parallel for shared (z, target_lat, target_long) private(i,rec_iter)
        for (i = 0; i < rec_count; i++){
                        rec_iter = sandbox+(i * REC_LENGTH + LATITUDE_POS - 1);
            float tmp_lat = atof(rec_iter);
            float tmp_long = atof(rec_iter+5);
                        z[i] = sqrt(( (tmp_lat-target_lat) * (tmp_lat-target_lat) )+( (tmp_long-target_long) * (tmp_long-target_long) ));
        }
