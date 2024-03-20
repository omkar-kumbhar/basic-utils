import os

# Step 1: Mount Google Drive to access its file system
def mount_google_drive():
    from google.colab import drive
    drive.mount('/content/drive')

mount_google_drive()

# Step 2: Install the virtualenv package to create virtual environments
os.system('pip install virtualenv')

# Step 3: Create a new virtual environment in your Google Drive for persistent storage
os.system('virtualenv /content/drive/MyDrive/colab_virtualenvs/deeplake_env')

# Step 4: Activate the virtual environment and install deeplake
os.system('bash -c "source /content/drive/MyDrive/colab_virtualenvs/deeplake_env/bin/activate; pip install deeplake"')

# Instructions for reusing the installed `deeplake` library in future Colab notebooks
reuse_instructions = """
# To reuse the installed `deeplake` library in future Colab notebooks, do the following:

1. Mount Google Drive:
from google.colab import drive
drive.mount('/content/drive')

2. Activate the virtual environment:
!source /content/drive/MyDrive/colab_virtualenvs/deeplake_env/bin/activate

3. Ensure Colab can access the Python packages in the virtual environment:
import sys
sys.path.append('/content/drive/MyDrive/colab_virtualenvs/deeplake_env/lib/python3.8/site-packages')

# You can now import `deeplake` and use it as needed in your notebook.
"""

print(reuse_instructions)
