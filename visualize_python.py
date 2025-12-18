import h5py
import numpy as np
import matplotlib.pyplot as plt

file_path = r'C:\Users\shale\OneDrive\Documents\GitHub\MST-plus-plus\predict_code\exp\mst_plus_plus\ARAD_1K_0912.mat'
file_path = r'C:\Users\shale\OneDrive\Documents\GitHub\MST-plus-plus\predict_code\exp\mst_plus_plus\frame1.mat'
file_path = r'C:\Users\shale\OneDrive\Documents\GitHub\MST-plus-plus\predict_code\exp\mst_plus_plus\frame2.mat'

with h5py.File(file_path, 'r') as f:
    # Load and transpose to (Height, Width, Bands)
    cube = np.array(f['cube']).transpose(2, 1, 0)

# We'll pick 4 bands that show the most contrast
# 0: Blue/Violet (Sky bright)
# 10: Cyan/Green
# 20: Orange/Red
# 30: Deep Red (Sky dark, Ground detailed)
selected_bands = [0, 10, 20, 30]
wavelengths = np.linspace(400, 700, 31)
q
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes = axes.flatten()

for i, band_idx in enumerate(selected_bands):
    # # Use 'jet' or 'viridis' if you want to see intensity better, 
    # # or 'gray' for a realistic look.q
    # im = axes[i].imshow(cube[:, :, band_idx], cmap='viridis')
    
    band_data = cube[:, :, band_idx]
    # --- CONTRAST BOOST ---
    # Ignore the extreme 2% of pixels to stop outliers from ruining the view
    vmin, vmax = np.percentile(band_data, [2, 98])
    
    im = axes[i].imshow(band_data, cmap='gray', vmin=vmin, vmax=vmax)
    # ----------------------
    
    nm = int(wavelengths[band_idx])
    axes[i].set_title(f"Band {band_idx} ({nm}nm)")
    axes[i].axis('off')
    
    # Add a colorbar to each to see the intensity scale
    plt.colorbar(im, ax=axes[i], fraction=0.046, pad=0.04)

plt.tight_layout()
plt.suptitle("Comparison of Spectral Bands: Sky vs. Ground", fontsize=16, y=1.02)
plt.show()