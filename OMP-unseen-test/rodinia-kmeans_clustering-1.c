            #pragma omp for \
                        private(i,j,index) \
                        firstprivate(npoints,nclusters,nfeatures) \
                        schedule(static) \
                        reduction(+:delta)
            for (i=0; i<npoints; i++) {
                /* find the index of nestest cluster centers */
                index = find_nearest_point(feature[i],
                             nfeatures,
                             clusters,
                             nclusters);
                /* if membership changes, increase delta by 1 */
                if (membership[i] != index) delta += 1.0;

                /* assign the membership to object i */
                membership[i] = index;

                /* update new cluster centers : sum of all objects located
                       within */
                partial_new_centers_len[tid][index]++;
                for (j=0; j<nfeatures; j++)
                       partial_new_centers[tid][index][j] += feature[i][j];
            }
