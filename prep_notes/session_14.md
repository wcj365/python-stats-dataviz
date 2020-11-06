## Prep Notes for Session 14
### Multiple subplots
```Python
fig, ax_list = plt.subplots(2,1,figsize=(12,8))  


# Make a double bar plot of size

ax_list[0]=tornado_size_decade.plot.bar("Decade")
ax_list[0].set_title("Size of Tornado")
ax_list[0].set_ylabel("Miles")

# Make a double line plot of size

ax_list[1]=tornado_size_decade.plot("Decade")
ax_list[1].set_title("Size of Tornado")
ax_list[1].set_ylabel("Miles")
```
### Descriptive Statistics
- Population & parameters
- Sample & statistics
- Centrality
- Dispersion
### Probability 
- Random variables
    - Discrete random variable
    - Continuous random variable
- Sampling
    - Non-random
    - Random sampling
- Probability
    - Theoretical Probability (population)
    - Empiricial Probability (sample)
- Probability Distributions 
### Foundation of Inferential Statistics
- Law of Large Numbers (LLN)
- Central Limit Theorem  (CLT)
### Inferential Statistics
- Point/Internal estimate
- Hypothesis testing
