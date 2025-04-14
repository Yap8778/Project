document.addEventListener('DOMContentLoaded', function() {
    // Elements
    const manualTab = document.getElementById('manual-tab');
    const imageTab = document.getElementById('image-tab');
    const manualContent = document.getElementById('manual-content');
    const imageContent = document.getElementById('image-content');
    const manualForm = document.getElementById('manual-form');
    const imageForm = document.getElementById('image-form');
    const cardInput = document.getElementById('card-number');
    const cardImage = document.getElementById('card-image');
    const uploadArea = document.getElementById('upload-area');
    const previewContainer = document.getElementById('preview-container');
    const imagePreview = document.getElementById('image-preview');
    const removeImageBtn = document.getElementById('remove-image');
    const resultContainer = document.getElementById('result-container');
    const closeResultBtn = document.getElementById('close-result');
    const statusText = document.getElementById('status-text');
    const validStatus = document.getElementById('valid-status');
    const cardTypeImg = document.getElementById('card-type-img');
    const cardTypeText = document.getElementById('card-type-text');
    const cardNumberDisplay = document.getElementById('card-number-display');

    // Card type images
    const cardImages = {
        visa: 'https://raw.githubusercontent.com/muhammederdem/credit-card-form/master/src/assets/images/visa.png',
        mastercard: 'https://raw.githubusercontent.com/muhammederdem/credit-card-form/master/src/assets/images/mastercard.png',
        amex: 'https://raw.githubusercontent.com/muhammederdem/credit-card-form/master/src/assets/images/amex.png',
        unknown: 'https://cdn-icons-png.flaticon.com/512/633/633611.png'
    };

    // Tab switching
    manualTab.addEventListener('click', function() {
        manualTab.classList.add('active');
        imageTab.classList.remove('active');
        manualContent.classList.remove('hidden');
        imageContent.classList.add('hidden');
    });

    imageTab.addEventListener('click', function() {
        imageTab.classList.add('active');
        manualTab.classList.remove('active');
        imageContent.classList.remove('hidden');
        manualContent.classList.add('hidden');
    });

    // Auto-format card input to add slashes after every 4 digits
    cardInput.addEventListener('input', function(e) {
        let value = e.target.value.replace(/\//g, ''); // Remove existing slashes
        let formattedValue = '';
        
        for (let i = 0; i < value.length; i++) {
            if (i > 0 && i % 4 === 0) {
                formattedValue += '/';
            }
            formattedValue += value[i];
        }
        
        // Update the input value with automatic formatting
        e.target.value = formattedValue;
    });

    // Manual form submission
    manualForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const cardNumber = cardInput.value.trim();
        
        if (!validateCardNumberFormat(cardNumber)) {
            showMatrix("Card format is incorrect. Please enter at least 16 digits.");
            return;
        }
        
        processCardTypeFirst(cardNumber);
    });

    // Image form submission
    imageForm.addEventListener('submit', function(e) {
        e.preventDefault();
        if (cardImage.files.length === 0) {
            showMatrix("Please upload an image first");
            return;
        }
        
        // In a real application, you would use OCR here to extract the card number
        // For demo purposes, we'll simulate OCR with a random valid card number
        const simulatedCardNumbers = [
            "4111/1111/1111/1111", // Visa (valid)
            "5500/0000/0000/0004", // Mastercard (valid)
            "3700/0000/0000/002",  // Amex (valid)
            "1234/5678/9012/3452"  // Unknown (invalid)
        ];
        
        const randomIndex = Math.floor(Math.random() * simulatedCardNumbers.length);
        const extractedCardNumber = simulatedCardNumbers[randomIndex];
        
        showMatrix(`Extracted card number: ${extractedCardNumber}`);
        processCardTypeFirst(extractedCardNumber);
    });

    // Image upload handling
    cardImage.addEventListener('change', function() {
        if (this.files && this.files[0]) {
            const reader = new FileReader();
            
            reader.onload = function(e) {
                imagePreview.src = e.target.result;
                previewContainer.classList.remove('hidden');
                uploadArea.style.borderColor = '#00ff00';
            };
            
            reader.readAsDataURL(this.files[0]);
        }
    });

    // Remove image
    removeImageBtn.addEventListener('click', function() {
        cardImage.value = '';
        previewContainer.classList.add('hidden');
        uploadArea.style.borderColor = '#00aa00';
    });

    // Close result
    closeResultBtn.addEventListener('click', function() {
        resultContainer.classList.add('hidden');
    });

    // Drag and drop for image upload
    ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
        uploadArea.addEventListener(eventName, preventDefaults, false);
    });

    function preventDefaults(e) {
        e.preventDefault();
        e.stopPropagation();
    }

    ['dragenter', 'dragover'].forEach(eventName => {
        uploadArea.addEventListener(eventName, highlight, false);
    });

    ['dragleave', 'drop'].forEach(eventName => {
        uploadArea.addEventListener(eventName, unhighlight, false);
    });

    function highlight() {
        uploadArea.style.borderColor = '#00ff00';
        uploadArea.style.backgroundColor = 'rgba(0, 40, 0, 0.3)';
    }

    function unhighlight() {
        uploadArea.style.borderColor = '#00aa00';
        uploadArea.style.backgroundColor = 'rgba(0, 20, 0, 0.3)';
    }

    uploadArea.addEventListener('drop', handleDrop, false);

    function handleDrop(e) {
        const dt = e.dataTransfer;
        const files = dt.files;
        
        if (files && files.length > 0) {
            cardImage.files = files;
            const event = new Event('change', { bubbles: true });
            cardImage.dispatchEvent(event);
        }
    }

    // Matrix-style message display
    function showMatrix(message) {
        // Create and style the message element
        const matrixMessage = document.createElement('div');
        matrixMessage.classList.add('matrix-message');
        matrixMessage.style.position = 'fixed';
        matrixMessage.style.top = '50%';
        matrixMessage.style.left = '50%';
        matrixMessage.style.transform = 'translate(-50%, -50%)';
        matrixMessage.style.backgroundColor = 'rgba(0, 20, 0, 0.9)';
        matrixMessage.style.color = '#00ff00';
        matrixMessage.style.padding = '20px';
        matrixMessage.style.borderRadius = '5px';
        matrixMessage.style.boxShadow = '0 0 20px rgba(0, 255, 0, 0.5)';
        matrixMessage.style.zIndex = '1000';
        matrixMessage.style.textAlign = 'center';
        matrixMessage.style.fontSize = '1.2rem';
        matrixMessage.style.fontFamily = "'Share Tech Mono', monospace";
        matrixMessage.style.maxWidth = '80%';
        
        // Animate text appearance character by character
        const chars = message.split('');
        matrixMessage.textContent = '';
        document.body.appendChild(matrixMessage);
        
        let i = 0;
        const interval = setInterval(() => {
            if (i < chars.length) {
                matrixMessage.textContent += chars[i];
                i++;
            } else {
                clearInterval(interval);
                
                // Remove message after a delay
                setTimeout(() => {
                    document.body.removeChild(matrixMessage);
                }, 3000);
            }
        }, 30);
    }

    // Card validation functions
    function validateCardNumberFormat(cardNumber) {
        // Check if matches the format (only numbers and /)
        const regex = /^[0-9/]+$/;
        if (!regex.test(cardNumber)) {
            return false;
        }
        
        // Replace / and check length
        const cleanNumber = cardNumber.replace(/\//g, '');
        return cleanNumber.length >= 16;
    }

    // New function to process card type first, then only validate if it's a known type
    function processCardTypeFirst(cardNumber) {
        // Clean the card number by removing /
        const cleanCardNumber = cardNumber.replace(/\//g, '');
        
        // Check the card type first
        const cardType = checkCardType(cleanCardNumber);
        
        // If card type is unknown, only show type without validation
        if (cardType === 'unknown') {
            displayResults(cardNumber, null, cardType);
            return;
        }
        
        // If it's a known card type, proceed with validation
        const isValid = luhnCheck(cleanCardNumber);
        
        // Display results with validation
        displayResults(cardNumber, isValid, cardType);
    }

    function luhnCheck(cardNumber) {
        // Implement the Luhn algorithm for card validation
        // This is based on the Step1.java logic
        
        // Reverse the card number
        const reversedCardNumber = cardNumber.split('').reverse().join('');
        let sum = 0;
        
        // Process each digit
        for (let i = 0; i < reversedCardNumber.length; i++) {
            let digit = parseInt(reversedCardNumber[i]);
            
            // If at even position (odd index in 0-based index)
            if (i % 2 !== 0) {
                digit *= 2;
                
                // If result is > 9, add the digits
                if (digit > 9) {
                    digit = Math.floor(digit / 10) + (digit % 10);
                }
            }
            
            sum += digit;
        }
        
        // Card is valid if sum is divisible by 10
        return sum % 10 === 0;
    }

    function checkCardType(cardNumber) {
        // Check card type based on the prefix (Step2.java logic)
        if (cardNumber.startsWith('4')) {
            return 'visa';
        } else if (cardNumber.startsWith('5')) {
            return 'mastercard';
        } else if (cardNumber.startsWith('37')) {
            return 'amex';
        } else {
            return 'unknown';
        }
    }

    function displayResults(cardNumber, isValid, cardType) {
        // Update the card type
        cardTypeImg.src = cardImages[cardType];
        cardTypeText.textContent = getCardTypeName(cardType);
        
        // Display the card number
        cardNumberDisplay.textContent = `Card Number: ${cardNumber}`;
        
        // Only show validation status for known card types
        if (cardType !== 'unknown') {
            statusText.textContent = isValid ? 'Valid' : 'Invalid';
            validStatus.classList.remove('valid', 'invalid', 'hidden');
            validStatus.classList.add(isValid ? 'valid' : 'invalid');
        } else {
            // Hide validation status for unknown card types
            validStatus.classList.add('hidden');
        }
        
        // Show the result container
        resultContainer.classList.remove('hidden');
    }

    function getCardTypeName(type) {
        switch(type) {
            case 'visa': return 'Visa Card';
            case 'mastercard': return 'Master Card';
            case 'amex': return 'American Express Card';
            default: return 'Unknown Card Type';
        }
    }
}); 