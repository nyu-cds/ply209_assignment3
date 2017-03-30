"""
    N-body simulation.

    Combined Optimizations + Numba Optimizations + Numpy/ufunc Optimizations
    Runtime: 13.204008617096634
    R = 101.76956199999995 / 13.204008617096634 = 7.70747467313
"""
import itertools
import timeit
from numba import jit, float64, float32, int64, int32, void, vectorize
import numpy as np

#Global Variables
PI = 3.14159265358979323
SOLAR_MASS = 4 * PI * PI
DAYS_PER_YEAR = 365.24

BODIES_INDEX = {
	'sun': 0,
	'jupiter': 1,
	'saturn': 2,
	'uranus': 3,
	'neptune': 4
	}

BODIES = np.array([
    ([0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [SOLAR_MASS, 0.0, 0.0]),

    ([4.84143144246472090e+00,
        -1.16032004402742839e+00,
        -1.03622044471123109e-01],
        [1.66007664274403694e-03 * DAYS_PER_YEAR,
        7.69901118419740425e-03 * DAYS_PER_YEAR,
        -6.90460016972063023e-05 * DAYS_PER_YEAR],
        [9.54791938424326609e-04 * SOLAR_MASS, 0.0, 0.0]),

    ([8.34336671824457987e+00,
        4.12479856412430479e+00,
        -4.03523417114321381e-01],
        [-2.76742510726862411e-03 * DAYS_PER_YEAR,
        4.99852801234917238e-03 * DAYS_PER_YEAR,
        2.30417297573763929e-05 * DAYS_PER_YEAR],
        [2.85885980666130812e-04 * SOLAR_MASS, 0.0, 0.0]),

    ([1.28943695621391310e+01,
        -1.51111514016986312e+01,
        -2.23307578892655734e-01],
        [2.96460137564761618e-03 * DAYS_PER_YEAR,
        2.37847173959480950e-03 * DAYS_PER_YEAR,
        -2.96589568540237556e-05 * DAYS_PER_YEAR],
        [4.36624404335156298e-05 * SOLAR_MASS, 0.0, 0.0]),

    ([1.53796971148509165e+01,
        -2.59193146099879641e+01,
        1.79258772950371181e-01],
        [2.68067772490389322e-03 * DAYS_PER_YEAR,
        1.62824170038242295e-03 * DAYS_PER_YEAR,
        -9.51592254519715870e-05 * DAYS_PER_YEAR],
        [5.15138902046611451e-05 * SOLAR_MASS, 0.0, 0.0])])
		
BODY_PAIRS = np.array(list(itertools.combinations(np.arange(BODIES.shape[0]), 2)))
		
@vectorize([float64(float64, float64)])
def vec_deltas(x, y):
    return x - y
	
@jit('void(float32, int32, float64[:,:,:], int32[:,:])', nopython=True)
def advance(dt, iterations, bodies, body_pairs):
    for _ in range(iterations):
        for body_pair_ind in range(len(body_pairs)):
            (body1, body2) = body_pairs[body_pair_ind]
    
            p1 = bodies[body1, 0]
            v1 = bodies[body1, 1]
            m1 = bodies[body1, 2, 0]
            p2 = bodies[body2, 0]
            v2 = bodies[body2, 1]
            m2 = bodies[body2, 2, 0]

            # Compute Deltas
            dp = vec_deltas(p1, p2)

            #update_vs compute_b(m2, dt, dx, dy, dz)
            mag = dt * (np.sum(dp**2) ** (-1.5))
            m1_mag = m1 * mag
            m2_mag = m2 * mag
            
            v1 -= dp * m2_mag
            v2 += dp * m1_mag
            
        for body in range(len(bodies)):
            r = bodies[body, 0]
            v = bodies[body, 1]

            #update_rs(r, dt, vx, vy, vz)
            r += dt * v

@jit('float64(float64[:,:,:] , int32[:,:], float64)', nopython=True) 
def report_energy(bodies, body_pairs, e=0.0):
    for body_pair_ind in range(len(body_pairs)):
        (body1, body2) = body_pairs[body_pair_ind]
    
        p1 = bodies[body1, 0]
        v1 = bodies[body1, 1]
        m1 = bodies[body1, 2, 0]
        p2 = bodies[body2, 0]
        v2 = bodies[body2, 1]
        m2 = bodies[body2, 2, 0]
        
        dp = vec_deltas(p1, p2)
        e -= (m1 * m2) / (np.sum(dp**2) ** 0.5)

    for body in range(len(bodies)):
        v = bodies[body, 1]
        m = bodies[body, 2, 0]
        
        e += m * np.sum(v**2) / 2.

    return e

@jit('void(int32, int32, int32, float64[:,:,:], int32[:,:])', nopython=True)
def nbody(loops, reference, iterations, bodies, body_pairs):
    '''
        nbody simulation
        loops - number of loops to run
        reference - body at center of system
        iterations - number of timesteps to advance
    '''
    #Offset momentum
    '''
        ref is the body in the center of the system
        offset values from this reference
    '''
    
    p = np.zeros(3)
    for body_ind in range(len(bodies)):
        v = bodies[body_ind, 1]
        m = bodies[body_ind, 2, 0]
        p -= v * m

    m = bodies[reference, 2, 0]
    bodies[reference, 1] = p / m

    for i in range(loops):
        advance(0.01, iterations, bodies, body_pairs)

        print(report_energy(bodies, body_pairs, 0.0))
		
if __name__ == '__main__':

	#Timing It
	print(timeit.timeit("nbody(100, BODIES_INDEX['sun'], 20000, BODIES, BODY_PAIRS)", setup="from __main__ import BODIES,nbody,BODIES_INDEX,BODY_PAIRS", number=1))
