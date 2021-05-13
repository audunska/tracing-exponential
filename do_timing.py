import random
import subprocess
import time
import math
import tqdm
import matplotlib.pyplot as plt
import numpy as np

def fun(n):
    return f"""pub async fn f{n}() -> Result<(), String> {{
    f{n+1}().await
}}
"""

def gen(num_instrument, err=False):
    instruments = random.sample(range(10), num_instrument)
    inst_str = "#[tracing::instrument" + ("(err)" if err else "") + "]\n"
    with open('src/gen.rs', 'w') as f:
        for n in range(10):
            if n in instruments:
                f.write(inst_str)
            f.write(fun(n))
        f.write("""
pub async fn f10() -> Result<(), String> {
    Ok(())
}
""")

def mean_std(times):
    mean = sum(times)/len(times)
    var = sum((t - mean)**2 for t in times)/(len(times)-1)
    return mean, math.sqrt(var)

def timeit():
    t = time.perf_counter()
    subprocess.run(["cargo", "build"], stderr=subprocess.DEVNULL)
    return time.perf_counter() - t

# First compile the deps
gen(0, False)
subprocess.run(["cargo", "build"])

samples = 2
max_instr = 3
means = []
stds = []
means_err = []
stds_err = []
for num_instrument in range(max_instr+1):
    print(f"num_instrument = {num_instrument}")
    times = []
    times_err = []
    for n in tqdm.tqdm(range(samples)):
        # Without (err)
        gen(num_instrument, False)
        times.append(timeit())

        # With (err)
        gen(num_instrument, True)
        times_err.append(timeit())

    mean, std = mean_std(times)
    means.append(mean)
    stds.append(std)

    mean, std = mean_std(times_err)
    means_err.append(mean)
    stds_err.append(std)

def plot(means, stds):
    means = np.array(means)
    plt.errorbar(range(1, len(means)), means[1:] - means[0], stds[1:])

plot(means, stds)
plot(means_err, stds_err)
plt.yscale('log')
plt.legend(['Without (err)', 'With (err)'])
plt.savefig('timing.png')
plt.show()

