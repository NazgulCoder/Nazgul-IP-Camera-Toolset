<?php
// Define the target folders where you want to delete old folders
$targetFolders = array(
    'CameraFTP/',
    'CameraFTP2/',
    // Add more folder paths as needed
);

// Define the age in days after which folders will be deleted
$ageThresholdInDays = 3; // Change this value to the desired age in days

// Calculate the time threshold in seconds based on the age threshold
$timeThreshold = time() - ($ageThresholdInDays * 24 * 60 * 60);

// Loop through each target folder
foreach ($targetFolders as $folderPath) {
    // Get all folder names within the current target folder
    $folders = glob($folderPath . '*', GLOB_ONLYDIR);

    // Loop through each folder
    foreach ($folders as $folder) {
        // Get the last modified time of the folder
        $lastModifiedTime = filemtime($folder);

        // Check if the folder is older than the specified age threshold
        if ($lastModifiedTime < $timeThreshold) {
            // Delete the folder and its contents recursively
            deleteFolder($folder);
        }
    }
}

/**
 * Function to delete a folder and its contents recursively.
 *
 * @param string $folderPath The path to the folder to be deleted.
 */
function deleteFolder($folderPath)
{
    if (is_dir($folderPath)) {
        $files = glob($folderPath . '/*');
        foreach ($files as $file) {
            is_dir($file) ? deleteFolder($file) : unlink($file);
        }
        rmdir($folderPath);
    }
}
?>
