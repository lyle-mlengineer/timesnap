function findYouTubeVideo() {
   const extractionContainer = document.getElementById('extractionContainer');
   const imageResult = document.getElementById('imageResult');
   const loadingContainer = document.getElementById('loadingContainer');
   const timestampsLoadingContainer = document.getElementById('timestampsLoadingContainer');
   const errorContainer = document.getElementById('errorMessage');
   const imageResultContainer = document.getElementById('imageResultContainer');
   const timestampsPre = document.getElementById('timestampsPre');
   const extractionActions = document.getElementById('extractionActions');

    // Hide error message and image result container
    errorContainer.classList.remove('show'); // Hide error message
    imageResultContainer.classList.remove('show'); // Hide image result container
    extractionActions.classList.remove('show'); // Hide extraction actions container
    // Reset previous results and show loading spinner
    imageResult.src = ''; // Clear previous image
    loadingContainer.classList.add('show'); // Show loading spinner
    timestampsLoadingContainer.classList.add('show'); // Show loading spinner for timestamps
   extractionContainer.classList.add('show'); // Add loading class to show the spinner

    const urlInput = document.getElementById('urlInput');
    const url = urlInput.value.trim();

    if (!url) {
        alert('Please enter a YouTube video URL.');
        loadingContainer.classList.remove('show'); // Hide loading spinner
        timestampsLoadingContainer.classList.remove('show'); // Hide loading spinner for timestamps
        return;
    }

    console.log('URL to extract timestamps from:', url);

    const formData = new FormData();
    formData.append('videourl', url);

   //  Send the URL to the backend for processing
    fetch('/api/v1/extract', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        // Display the extracted timestamps
        imageResult.src = data.thumbnail_url; // Set the thumbnail image
        timestampsPre.textContent = JSON.stringify(data.timestamps, null, 2); // Display timestamps in the pre element
        loadingContainer.classList.remove('show'); // Hide loading spinner
        timestampsLoadingContainer.classList.remove('show'); // Hide loading spinner for timestamps
        imageResultContainer.classList.add('show'); // Show image result container
        extractionActions.classList.add('show'); // Show extraction actions container
      //   const resultContainer = document.getElementById('resultContainer');
      //   resultContainer.innerHTML = ''; // Clear previous results

      //   if (data.timestamps && data.timestamps.length > 0) {
      //       data.timestamps.forEach(timestamp => {
      //           const timestampElement = document.createElement('div');
      //           timestampElement.textContent = timestamp;
      //           resultContainer.appendChild(timestampElement);
      //       });
      //   } else {
      //       resultContainer.textContent = 'No timestamps found.';
      //   }
      console.log('Extracted timestamps:', data.timestamps);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

const copyTimestampsButton = document.getElementById('copyTimestampsButton');
copyTimestampsButton.addEventListener('click', () => {
    const timestampsPre = document.getElementById('timestampsPre');
    const timestampsText = timestampsPre.textContent;

    navigator.clipboard.writeText(timestampsText)
        .then(() => {
            alert('Timestamps copied to clipboard!');
        })
        .catch(err => {
            console.error('Failed to copy timestamps: ', err);
        });
});

function downloadTimestamps() {
    const timestampsPre = document.getElementById('timestampsPre');
    const timestampsText = timestampsPre.textContent;
    const blob = new Blob([timestampsText], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'timestamps.json';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
}