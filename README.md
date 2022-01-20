# Shopify-Backend-Intern-Challenge-2022

## Prerequisites: 
- Python 3.9.x
- Windows 10
    - Note: This was built and tested in Windows 10, and so I do not have the ability to verify it works on other operating systems. I will provide Linux/Unix equivalent instructions, but cannot guarantee they work.
    
## Instructions
1. Download this project.
2. Open terminal application of choice (CMD or PowerShell), and navigate to the root directory of the project: `[where did you put it]/Shopify-Backend-Intern-Challenge-2022/`
3. Run the appropriate activation script for the virtual environment, located in `/Shopify-Backend-Intern-Challenge-2022/inventory-env/Scripts/`
   - **Windows CMD**, the necessary script is `activate.bat`
   - **Windows POWERSHELL**, the necessary script is `activate.ps1`
   - **Linux**: file is simply `activate`
4. Verify the virtual environment has been successfully activated (should show `(inventory-env)` in front of the working directory name in terminal).
5. Navigate to `/Shopify-Backend-Intern-Challenge-2022/inventory-project/`
6. Start the local server by running `python -m manage runserver`
    - Linux: `python manage.py runserver`
7. The web application will then be accessible at `http://localhost:8000/inventoryapp/`.

### Notes
If later on some packages appear to be missing, return to project root directory and run `python -m pip install -r requirements.txt` to redownload necessary packages. Linux equivalent should be `pip install -r requirements.txt`.
