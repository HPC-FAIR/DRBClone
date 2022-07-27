# Microbenchmark property labels (P-Labels)

P-Label | Meaning (microbenchmarks with data races)  | P-Label | Meaning (microbenchmarks without data races)
------|-----------------------------------|------|------------------------------
  Y1  | Unresolvable dependences          |  N1  | Embarrassingly parallel or single thread execution
  Y2  | Missing data sharing clauses      |  N2  | Use of data sharing clauses
  Y3  | Missing synchronization           |  N3  | Use of synchronization
  Y4  | SIMD data races                   |  N4  | Use of SIMD directives
  Y5  | Accelerator data races            |  N5  | Use of accelerator directives
  Y6  | Undefined behavior                |  N6  | Use of special language features
  Y7  | Numerical kernel data races       |  N7  | Numerical kernels


# Microbenchmarks with known data races (some have a varying length version)

Microbenchmark                                      |P-Label| Description                                                                  											| Source     
----------------------------------------------------|-------|-----------------------------------------------------------------------------------------------------------------------|----------
DRB001-antidep1-orig-yes.c                          |Y1     | Anti-dependence within a single loop                                         											| AutoPar    
DRB002-antidep1-var-yes.c                           |Y1     | Anti-dependence within a single loop                                         											| AutoPar    
DRB003-antidep2-orig-yes.c                          |Y1     | Anti-dependence within a two-level loop nest                                 											| AutoPar    
DRB004-antidep2-var-yes.c                           |Y1     | Anti-dependence within a two-level loop nest                                 											| AutoPar    
DRB005-indirectaccess1-orig-yes.c                   |Y7     | Indirect access with overlapped index array elements                         											| LLNL App   
DRB006-indirectaccess2-orig-yes.c                   |Y7     | Overlapping index array elements when 36 or more threads are used            											| LLNL App   
DRB007-indirectaccess3-orig-yes.c                   |Y7     | Overlapping index array elements when 60 or more threads are used            											| LLNL App   
DRB008-indirectaccess4-orig-yes.c                   |Y7     | Overlapping index array elements when 180 or more threads are used           											| LLNL App   
DRB009-lastprivatemissing-orig-yes.c                |Y2     | Data race due to a missing `lastprivate()` clause                            											| AutoPar    
DRB010-lastprivatemissing-var-yes.c                 |Y2     | Data race due to a missing `lastprivate()` clause                            											| AutoPar    
DRB011-minusminus-orig-yes.c                        |Y3     | Unprotected decrement operation `--`                                         											| AutoPar    
DRB012-minusminus-var-yes.c                         |Y3     | Unprotected decrement operation `--`                                         											| AutoPar    
DRB013-nowait-orig-yes.c                            |Y3     | Missing barrier due to a wrongfully used nowait                              											| AutoPar    
DRB014-outofbounds-orig-yes.c                       |Y6     | Out of bound access of the 2nd dimension of array                            											| AutoPar    
DRB015-outofbounds-var-yes.c                        |Y6     | Out of bound access of the 2nd dimension of array                            											| AutoPar    
DRB016-outputdep-orig-yes.c                         |Y1     | Output dependence and true dependence within a loop                          											| AutoPar    
DRB017-outputdep-var-yes.c                          |Y1     | Output dependence and true dependence within a loop                          											| AutoPar    
DRB018-plusplus-orig-yes.c                          |Y1     | increment operation `++` on array index variable                             											| AutoPar    
DRB019-plusplus-var-yes.c                           |Y1     | increment operation `++` on array index variable                             											| AutoPar    
DRB020-privatemissing-orig-yes.c                    |Y2     | Missing `private()` for a temp variable                                      											| AutoPar    
DRB021-privatemissing-var-yes.c                     |Y2     | Missing `private()` for a temp variable                                      											| AutoPar    
DRB022-reductionmissing-orig-yes.c                  |Y2     | Missing `reduction()` for a variable                                         											| AutoPar    
DRB023-reductionmissing-var-yes.c                   |Y2     | Missing `reduction()` for a variable                                         											| AutoPar    
DRB024-sections1-orig-yes.c                         |Y3     | Unprotected data writes in parallel sections                                 											| New        
DRB025-simdtruedep-orig-yes.c                       |Y1,Y4  | SIMD instruction level data races                                            											| New        
DRB026-simdtruedep-var-yes.c                        |Y1,Y4  | SIMD instruction level data races                                            											| New        
DRB027-targetparallelfor-orig-yes.c                 |Y1,Y5  | Data races in loops offloaded to accelerators                                											| New        
DRB028-taskdependmissing-orig-yes.c                 |Y3     | Unprotected data writes in two tasks                                         											| New        
DRB029-truedep1-orig-yes.c                          |Y1     | True data dependence among multiple array elements within a single level loop											| AutoPar    
DRB030-truedep1-var-yes.c                           |Y1     | True data dependence among multiple array elements within a single level loop											| AutoPar    
DRB031-truedepfirstdimension-(orig&#124;var)-yes.c  |Y1     | True data dependence of first dimension for a 2-D array accesses             											| AutoPar    
DRB032-truedepfirstdimension-(orig&#124;var)-yes.c  |Y1     | True data dependence of first dimension for a 2-D array accesses             											| AutoPar    
DRB033-truedeplinear-orig-yes.c                     |Y1     | Linear equation as array subscript                                           											| AutoPar    
DRB034-truedeplinear-var-yes.c                      |Y1     | Linear equation as array subscript                                           											| AutoPar    
DRB035-truedepscalar-orig-yes.c                     |Y1     | True data dependence due to scalar                                           											| AutoPar    
DRB036-truedepscalar-var-yes.c                      |Y1     | True data dependence due to scalar                                           											| AutoPar    
DRB037-truedepseconddimension-(orig&#124;var)-yes.c |Y1     | True data dependence on 2nd dimension of a 2-D array accesses                											| AutoPar    
DRB038-truedepseconddimension-(orig&#124;var)-yes.c |Y1     | True data dependence on 2nd dimension of a 2-D array accesses                											| AutoPar    
DRB039-truedepsingleelement-(orig&#124;var)-yes.c   |Y1     | True data dependence due to a single array element                           											| AutoPar    
DRB040-truedepsingleelement-(orig&#124;var)-yes.c   |Y1     | True data dependence due to a single array element                           											| AutoPar    
DRB073-doall2-orig-yes.c                            |Y2     | Missing `private()` for inner loop nest's loop index variable                											| New        
DRB074-flush-orig-yes.c                             |Y2     | Reduction using a shared variable, extracted from an official OpenMP example 											| New        
DRB075-getthreadnum-orig-yes.c                      |Y1     | Work sharing within one branch of a `if` statement                           											| New        
DRB080-func-arg-orig-yes.c                          |Y6     | Function arguments passed by reference, inheriting shared attribute          											| New        
DRB082-declared-in-func-orig-yes.c                  |Y6     | A variable declared within a function called by a parallel region            											| New
DRB084-threadprivatemissing-orig-yes.c              |Y2     | Missing threadprivate for a global var, not referenced within a construct    											| New
DRB086-static-data-member-orig-yes.cpp              |Y2     | Missing threadprivate for a static member, not referenced within a construct 											| New
DRB087-static-data-member2-orig-yes.cpp             |Y2     | Missing threadprivate for a static member, referenced within a construct     											| New
DRB088-dynamic-storage-orig-yes.c                   |Y2     | Data race for a dynamica storage variable, not referenced within a construct 											| New
DRB089-dynamic-storage2-orig-yes.c                  |Y2     | Data race for a dynamica storage variable, referenced within a construct     											| New
DRB090-static-local-orig-yes.c                      |Y2     | Data race for a locally declared static variable                             											| New
DRB092-threadprivatemissing2-orig-yes.c             |Y2     | Missing threadprivate for a variable referenced within a construct           											| New
DRB095-doall2-taskloop-orig-yes.c                   |Y2     | Missing protection for inner loop's loop variable                            											| New
DRB106-taskwaitmissing-orig-yes.c                   |Y3     | Missing taskwait to ensure correct order of calculations                     											| New
DRB109-orderedmissing-orig-yes.c                    |Y3     | Missing the ordered clause, causing data races                               											| New
DRB111-linearmissing-orig-yes.c                     |Y2     | Missing linear for a shared variable, causing data races                     											| New               
DRB114-if-orig-yes.c                                |Y1     | True data dependence within a single level loop, with if() clause            											| New
DRB115-forsimd-orig-yes.c                           |Y1,Y4  | Both thread and instruction level data races due to omp loop simd            											| New
DRB116-target-teams-orig-yes.c                      |Y3     | Master threads of two teams do not have synchronization, causing data races  											| New
DRB117-taskwait-waitonlychild-orig-yes.c            |Y3	    | Thread encountering the taskwait is only waiting for the child task's completion, not the descendant tasks.							| New
DRB119-nestlock-orig-yes.c                          |Y3	    | Missing omp_set_nest_lock() on a function called at multiple points. 												| New
DRB123-taskundeferred-orig-yes.c                    |Y6	    | A single thread spawning multiple tasks due to missing if(0)													| New
DRB124-master-orig-yes.c                            |Y3	    | Master construct does not have an implicit barrier. 														| New
DRB129-mergeable-taskwait-orig-yes.c                |Y2	    | Created task will access different instances of a variable depending on the mergeable status. Missing shared clause. 						| New
DRB131-taskdep4-orig-omp45-yes.c                    |Y3	    | Accessing a variable before the completion of the operation. Missing taskwait. 											| New
DRB134-taskdep5-orig-omp45-yes.c                    |Y1	    | Operation depends on two variables, but the depend clause is mentioned only for one variable. 									| New
DRB136-taskdep-mutexinoutset-orig-yes.c	            |Y1,Y6  | Missing mutexinoutset dependence type on a variable. Undefined execution order. 											| OpenMP Official Examples
DRB138-simdsafelen-orig-yes.c                       |Y6	    | Parameter for safelen() clause having a value lesser than required for a defined execution. 									| New
DRB140-reduction-barrier-orig-yes.c                 |Y3	    | Asynchronous update by master directive and usage in reduction clause. 												| New
DRB142-acquirerelease-orig-yes.c                    |Y3	    | Missing implicit flush after critical construct.															| New
DRB144-critical-missingreduction-orig-gpu-yes.c	    |Y5, Y3 | Asynchronous update of a variable across teams due to improper critical and atomic construct usage. 								| New
DRB148-critical1-orig-gpu-yes.c                     |Y5, Y3 | Due to different locks, addition and subtraction interleave. 													| DRACC
DRB150-missinglock1-orig-gpu-yes.c                  |Y5, Y3 | distribute parallel for directive executes across teams. omp_set_lock() ensures synchronization only within a team. 						| DRACC
DRB151-missinglock3-orig-gpu-yes.c                  |Y5, Y3 | Missing synchronization in teams distribute parallel for construct among a team of threads. 									| DRACC
DRB153-missinglock2-orig-gpu-yes.c                  |Y5, Y2 | Concurrent access of a variable in an intra region with locks leading to intra region data race. 									| DRACC
DRB156-missingordered-orig-gpu-yes.c                |Y5, Y6 | Execution on accelerators with missing ordered directive causes data race.											| DRACC
DRB157-missingorderedsimd-orig-gpu-yes.c            |Y5, Y4 | Missing synchronization on accelerator due to simd directive. 													| DRACC
DRB160-nobarrier-orig-gpu-yes.c                     |Y5, Y3 | Missing implicit barrier due to distribute directive. 														| DRACC
DRB161-nolocksimd-orig-gpu-yes.c                    |Y5, Y3 | Concurrent access on a counter with no lock with simd—atomicity Violation.											| DRACC
DRB164-simdmissinglock1-orig-gpu-yes.c              |Y5, Y3 | Concurrent access on a counter with no lock with simd across teams. Inter-region data race									| DRACC
DRB165-taskdep4-orig-omp50-yes.c                    |Y3	    | Missing taskwait. Accessing a variable before task completion. 													| OpenMP Official Examples
DRB168-taskdep5-orig-omp50-yes.c                    |Y1	    | OpenMP depend clause for only one variable in a bivariate equation. 												| OpenMP Official Examples
DRB169-missingsyncwrite-orig-yes.c                  |Y6	    | Missing parallell construct for write                                												| NAS Parallel Benchmarkss
DRB173-non-sibling-taskdep-yes.c                    |Y6	    | Non-sibling tasks with declared task dependency                     												| New
DRB175-non-sibling-taskdep2-yes.c                   |Y6	    | Non-sibling tasks with declared task dependency                     												| New
DRB177-fib-taskdep-yes.c                            |Y6	    | Race due to scale problem size by providing size argument           												| Fibonacci Code
DRB178-input-dependence-var-yes.c                   |Y1	    | Input dependence race                                               												| OMPRacer
DRB179-thread-sensitivity-yes.cc                    |Y6	    | Conflicting writes to same address                                  												| New
DRB180-miniAMR-yes.c                                |Y6	    | Race by shared index variable                                       												| MiniAMR app               
DRB181-SmithWaterman-yes.c                          |Y6	    | Race appears with larger data size                                  												| Smith-Waterman app


# Microbenchmarks without known data races

Microbenchmark                           |P-Label    | Description                                                                          									| Source     
-----------------------------------------|-----------|--------------------------------------------------------------------------------------------------------------------------|------------
DRB041-3mm-parallel-no.c                 |N2     	 | 3-step matrix-matrix multiplication, non-optimized version                           									| Polyhedral 
DRB042-3mm-tile-no.c                     |N2,N4  	 | 3-step matrix-matrix multiplication, with tiling and nested SIMD                     									| Polyhedral 
DRB043-adi-parallel-no.c                 |N2     	 | Alternating Direction Implicit solver, non-optimized version                         									| Polyhedral  
DRB044-adi-tile-no.c                     |N2,N4  	 | Alternating Direction Implicit solver, with tiling and nested SIMD                   									| Polyhedral  
DRB045-doall1-orig-no.c                  |N1     	 | Classic DOAll loop operating on a one dimensional array                              									| AutoPar    
DRB046-doall2-orig-no.c                  |N1     	 | Classic DOAll loop operating on a two dimensional array                              									| AutoPar     
DRB047-doallchar-orig-no.c               |N1     	 | Classic DOALL loop operating on a character array                                    									| New        
DRB048-firstprivate-orig-no.c            |N2     	 | Example use of firstprivate                                                          									| AutoPar    
DRB049-fprintf-orig-no.c                 |N6     	 | Use of `fprintf()`                                                                   									| New        
DRB050-functionparameter-orig-no.c       |N6     	 | Arrays passed as function parameters                                                 									| LLNL App   
DRB051-getthreadnum-orig-no.c            |N2     	 | single thread execution using `if (omp_get_thread_num()==0)`                         									| New              
DRB052-indirectaccesssharebase-orig-no.c |N7     	 | Indirect array accesses using index arrays without overlapping                       									| LLNL App   
DRB053-inneronly1-orig-no.c              |N1     	 | Two-level nested loops, inner level is parallelizable. Anti dependence on outer level									| AutoPar    
DRB054-inneronly2-orig-no.c              |N1     	 | Two-level nested loops, inner level is parallelizable. True dependence on outer level									| AutoPar    
DRB055-jacobi2d-parallel-no.c            |N7     	 | Jacobi with array copying, no reduction, non-optimized version                       									| Polyhedral 
DRB056-jacobi2d-tile-no.c                |N4,N7  	 | Jacobi with array copying, no reduction, with tiling and nested SIMD                 									| Polyhedral 
DRB057-jacobiinitialize-orig-no.c        |N7     	 | The array initialization parallel loop in Jacobi                                     									| AutoPar    
DRB058-jacobikernel-orig-no.c            |N7     	 | Parallel Jacobi stencil computation kernel with array copying and reduction          									| AutoPar    
DRB059-lastprivate-orig-no.c             |N2     	 | Example use of lastprivate                                                           									| AutoPar    
DRB060-matrixmultiply-orig-no.c          |N7     	 | Classic i-k-j order matrix multiplication using OpenMP                               									| AutoPar    
DRB061-matrixvector1-orig-no.c           |N7     	 | Matrix-vector multiplication parallelized at the outer level loop                    									| AutoPar    
DRB062-matrixvector2-orig-no.c           |N7     	 | Matrix-vector multiplication parallelized at the inner level loop with reduction     									| AutoPar    
DRB063-outeronly1-orig-no.c              |N2     	 | Two-level nested loops, outer level is parallelizable. Anti dependence on inner level									| AutoPar    
DRB064-outeronly2-orig-no.c              |N2     	 | Two-level nested loops, outer level is parallelizable. True dependence on inner level									| AutoPar    
DRB065-pireduction-orig-no.c             |N7     	 | PI calculation using reduction                                                       									| AutoPar    
DRB066-pointernoaliasing-orig-no.c       |N6     	 | Pointers assigned by different malloc calls, without aliasing                        									| LLNL App   
DRB067-restrictpointer1-orig-no.c        |N6     	 | C99 restrict pointers used for array initialization, no aliasing                     									| LLNL App    
DRB068-restrictpointer2-orig-no.c        |N6     	 | C99 restrict pointers used for array computation, no aliasing                        									| LLNL App   
DRB069-sectionslock1-orig-no.c           |N3     	 | OpenMP parallel sections with a lock to protect shared data writes                   									| New        
DRB070-simd1-orig-no.c                   |N1,N4  	 | OpenMP SIMD directive to indicate vectorization of a loop                            									| New        
DRB071-targetparallelfor-orig-no.c       |N1,N5  	 | No data races in loops offloaded to accelerators                                     									| New        
DRB072-taskdep1-orig-no.c                |N3     	 | OpenMP task with depend clauses to avoid data races                                  									| New         
DRB076-flush-orig-no.c                   |N2     	 | OpenMP private clause to avoid data races                                            									| New         
DRB077-single-orig-no.c                  |N1     	 | OpenMP single directive to use only one thread for execution                         									| New
DRB078-taskdep2-orig-no.c                |N3     	 | OpenMP task depend clause to avoid data races                                        									| New         
DRB079-taskdep3-orig-no.c                |N3     	 | OpenMP task depend clause to avoid data races                                        									| New         
DRB081-func-arg-orig-no.c                |N6     	 | Function arguments passed by value, private                                          									| New        
DRB083-declared-in-func-orig-no.c        |N6     	 | A variable declared within a function called by a parallel region                    									| New
DRB085-threadprivate-orig-no.c           |N2     	 | Use threadprivate to protect a file scope variable, not referenced within a construct       									| New
DRB091-threadprivate2-orig-no.c          |N2     	 | Use threadprivate to protect a file scope variable, referenced within a construct           									| New
DRB093-doall2-collapse-orig-no.c         |N2     	 | Use collapse(n) to control the number of associated loops of omp for                        									| New
DRB094-doall2-ordered-orig-no.c          |N2     	 | Use ordered(n) to control the number of associated loops of omp for                         									| New
DRB096-doall2-taskloop-collapse-orig-no.c|N2     	 | Use ordered(n) to control the number of associated loops of taskloop                        									| New
DRB097-target-teams-distribute-orig-no.c |N2     	 | Predetermined attribute rule for loop variable associated with distribute                   									| New
DRB098-simd2-orig-no.c                   |N1,N2  	 | OpenMP SIMD directive to indicate vectorization of two nested loops                         									| New        
DRB099-targetparallelfor2-orig-no.c      |N1,N5  	 | Loops offloaded to accelerators: array sections derived from pointer                        									| New        
DRB100-task-reference-orig-no.cpp        |N1     	 | OpenMP 4.5 feature: orphaned task generating construct using pass-by-reference              									| New
DRB101-task-value-orig-no.cpp            |N1     	 | In a task generating construct, a variable without applicable rules is firstprivate         									| New
DRB102-copyprivate-orig-no.c             |N2     	 | threadprivate+copyprivate, a variable without applicable rules is firstprivate              									| New
DRB103-master-orig-no.c                  |N1     	 | master directive to ensure only one thread will execute data accesses                       									| New
DRB104-nowait-barrier-orig-no.c          |N3     	 | Use barrier to ensure correct order of initialization and assignment phases                 									| New
DRB105-taskwait-orig-no.c                |N3     	 | Use taskwait to ensure correct order of tasks                                               									| New
DRB107-taskgroup-orig-no.c               |N3     	 | Use taskgroup to ensure correct order of tasks                                              									| New
DRB108-atomic-orig-no.c                  |N3     	 | Use atomic to protect shared accesses to a variable                                         									| New
DRB110-ordered-orig-no.c                 |N3     	 | Proper use of the ordered clause to avoid data races                                        									| New
DRB112-linear-orig-no.c                  |N2     	 | Use linear to privatize a variable                                                          									| New
DRB113-default-orig-no.c                 |N1     	 | default(none) to enforce explicitly listing variables in data-sharing clauses               									| New
DRB118-nestlock-orig-no.c                |N3	 	 | Use of omp_set_nest_lock to be able to lock several times. Extracted from an official OpenMP example 							| OpenMP Official Example
DRB120-barrier-orig-no.c                 |N3	 	 | Use barrier to ensure the correct order of increment ops.													| New
DRB121-reduction-orig-no.c               |N2	 	 | Use reduction clause to get the correct sum within a parallel region. 											| New
DRB122-taskundeferred-orig-no.c          |N6	 	 | Undeferred all the tasks using if(0) 															| OpenMP Official Example
DRB125-single-orig-no.c                  |N1	 	 | Single construct usage to have implicit barrier, private.													| New
DRB126-firstprivatesections-orig-no.c    |N1	 	 | Use of firstprivate and omp_set_num_threads() to ensure that the same thread executes both the sections. 							| New
DRB127-tasking-threadprivate1-orig-no.c  |N1	 	 | Order execution is undefined. There is a race condition but no data race. 											| New
DRB128-tasking-threadprivate2-orig-no.c  |N1	 	 | Restricting update to a threadprivate variable. 														| New
DRB130-mergeable-taskwait-orig-no.c      |N2	 	 | Use of mergeable construct on a shared variable ensures that the outcome does not depend on task's merged status.						| New
DRB132-taskdep4-orig-omp45-no.c          |N3, N1	 | Accessing a variable safely after taskwait directive, two variables. OpenMP 4.5 compliant. 									| New
DRB133-taskdep5-orig-omp45-no.c          |N3		 | Accessing a variable safely after taskwait directive, single variable. OpenMP 4.5 compliant. 								| New
DRB135-taskdep-mutexinoutset-orig-no.c   |N1		 | Use of mutexinoutset in depend clause to avoid data race. 													| OpenMP Official Example
DRB137-simdsafelen-orig-no.c             |N1		 | Use of safelen construct to avoid udnefined behavior. 													| New
DRB139-worksharingcritical-orig-no.c     |N1		 | Use of single directive inside a nested parallel region within a critical construct. 									| New
DRB141-reduction-barrier-orig-no.c       |N3		 | Addition of explicit barrier to ensure completion of initialization of a variable before encountering a parallel region.					| New
DRB143-acquirerelease-orig-no.c          |N3		 | Use of flush after critical construct to avoid data race.													| New
DRB145-atomiccritical-orig-gpu-no.c      |N5, N2	 | Use of reduction construct to synchronize across teams. 													| New
DRB146-atomicupdate-orig-gpu-no.c        |N5, N3, N1 | Use of atomic update construct to have synchronization across teams. 												| New
DRB147-critical1-orig-gpu-no.c           |N5, N1	 | To have synchronization across distribute parallel loop across teams, usage of atomic construct.								| New
DRB149-missingdata1-orig-gpu-no.c        |N5		 | Classic i-k-j matrix multiplication on accelerator. 														| New
DRB152-missinglock2-orig-gpu-no.c        |N5, N3	 | Use of omp_set_lock() to synchronize within a team.														| New
DRB154-missinglock3-orig-gpu-no.c        |N5, N3	 | Use omp_set_lock() and reduction construct to avoid atomicity violations across teams on accelerators. 							| New
DRB155-missingordered-orig-gpu-no.c      |N5, N1	 | Proper use of the ordered clause to avoid data races, ensuring sequential consistency. 									| New
DRB158-missingtaskbarrier-orig-gpu-no.c  |N5, N1	 | Use of depend clause to ensure correct execution sequence.													| New
DRB159-nobarrier-orig-gpu-no.c           |N5, N3	 | Vector addition and multiplication employing the same variable should have a barrier in between.								| New
DRB162-nolocksimd-orig-gpu-no.c          |N5, N4	 | Use reduction clause to avoid concurrent access on a variable due to exceeding permitted threads usage per warp limit.					| New
DRB163-simdmissinglock1-orig-gpu-no.c    |N5, N4	 | SIMD directive indicates vectorization of a loop on the accelerator; usage of reduction to ensure no data race. 						| New
DRB166-taskdep4-orig-omp50-no.c          |N1		 | Use of takwait to avoid data race due to access before decrement operation. OpenMP 5.0 compliant. 								| OpenMP Official Example
DRB167-taskdep4-orig-omp50-no.c          |N1		 | Dependency on two variables but defined only on one. Use of taskwait ensures no data race. OpenMP5.0 compliant. 						| OpenMP Official Example
DRB170-nestedloops-orig-no.c             |N2		 | Use of private clause to ensure no data race                                                                    						| NAS Benchmark
DRB171-threadprivate3-orig-no.c          |N1		 |  example of a threadprivate var and update by TID==0 only                                                       						| NAS Benchmark           
DRB172-critical2-orig-no.c               |N2, N3 	 | Use of private and explicit barrier tto ensure no data race.                                                    						| NAS Benchmark
DRB174-non-sibling-taskdep-no.c          |N3		 | Use of taskwait ensures no data race. 															| New
DRB176-fib-taskdep-no.c                  |N3		 | Fibonacci code with proper task dependency.                                                                     						| Fibonacci code
