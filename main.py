import os
import subprocess

# Path to the folder containing .aup3 files
input_folder = r"D:\ready\exported\unprocessed"
output_folder = r"D:\ready\exported\processed"

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Path to Audacity's executable (modify if necessary)
audacity_exe = r"C:\Program Files\Audacity\audacity.exe"

# Nyquist script for increasing volume
nyquist_script = "(mult 2.0 s)"

# Desired MP3 quality (adjust as needed)
mp3_quality = 2  # 0 = highest, 9 = lowest

# Process each .aup3 file
for file in os.listdir(input_folder):
    if file.endswith(".aup3"):
        input_file = os.path.join(input_folder, file)
        output_file = os.path.join(output_folder, file.replace(".aup3", ".mp3"))

        # Audacity scripting command to apply the Nyquist effect and export
        commands = f"""
        SelectAll:
        ApplyNyquistPrompt: Command="{nyquist_script}"
        Export2: Filename="{output_file}" Format="MP3" Options="MP3Quality={mp3_quality}"
        """
        script_path = os.path.join(output_folder, "commands.txt")
        
        # Save commands to a temporary file
        with open(script_path, "w") as script_file:
            script_file.write(commands)
        
        # Call Audacity in scripting mode
        subprocess.run([audacity_exe, "--batch", "--quit-after-closing", script_path])
        
        # Cleanup
        os.remove(script_path)

print("Batch processing completed!")
