// script.js

// Function to save entries to the API
async function saveEntry(entry) {
    try {
        const response = await fetch('https://api.example.com/entries', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(entry),
        });
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json();
        console.log('Entry saved:', data);
    } catch (error) {
        console.error('Error saving entry:', error);
    }
}

// Function to load entries from the API
async function loadEntries() {
    try {
        const response = await fetch('https://api.example.com/entries');
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const entries = await response.json();
        console.log('Entries loaded:', entries);
    } catch (error) {
        console.error('Error loading entries:', error);
    }
}