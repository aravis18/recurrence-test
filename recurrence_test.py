#%%
z = []
z.insert(0,7)
#%%
for i in range(0,100):
    z[0] = 7
    z[i] = (z[i-1] + 3)%25
    # z.append(z[i])
    z.insert(i,z[i])

# %%
print(z)
print(len(z))
#%%
for i in range(0,100):
    if z[0] == z[i]:
        print(i)
# %%
