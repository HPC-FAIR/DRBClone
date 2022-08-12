        #pragma omp parallel for num_threads(omp_num_threads)
        for (i = 0; i < img_in->m; i++) {
                int j, el_i, el_j, x, y;
                for (j = 0; j < img_in->n; j++) {
                        double max = 0.0, temp;
                        for (el_i = 0; el_i < strel->m; el_i++) {
                                for (el_j = 0; el_j < strel->n; el_j++) {
                                        y = i - el_center_i + el_i;
                                        x = j - el_center_j + el_j;
                                        if (y >=0 && x >= 0 && y < img_in->m && x < img_in->n && m_get_val(strel, el_i, el_j) != 0) {
                                                temp = m_get_val(img_in, y, x);
                                                if (temp > max) max = temp;
                                        }
                                }
                        }
                        m_set_val(dilated, i, j, max);
                }
        }
