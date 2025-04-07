/*-------------------------Sidebar-------------------------------------------*/

function openSidebar() { 
    document.getElementById("sidebar").style.width = "250px";
}

function closeSidebar() {
    document.getElementById("sidebar").style.width = "0";
}


/*-------------------------Hero section-------------------------------------------*/

document.querySelector('.primary')?.addEventListener('click', function() {
    alert('Navigate to Registration Page');
});
document.querySelector('.secondary').addEventListener('click', function() {
    alert('Navigate to About Us Page');
});








/*----------------------------Login form AND Register form---------------------------------------------*/ 


function openForm(formId) 
                {
                    // Get all elements with class 'form-popup-R'
                    let forms = document.getElementsByClassName('form-popup');

                    // Loop through each form and hide it
                    for (let i = 0; i < forms.length; i++) 
                    {
                        forms[i].style.display = 'none';
                    }

                    // Show the selected form
                    document.getElementById(formId).style.display = 'block';
                }



/*----------------------------------------------------BROWSE TASK---------------------------------------------------------------------- */            

function handleGoogleSignIn(response) {
    // Get the ID token from the response
    const idToken = response.credential;
    console.log("Google ID Token:", idToken);
    
    // Here you would send this token to your server
    // Example:
    /*
    fetch('/auth/google', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ token: idToken })
    })
    .then(response => response.json())
    .then(data => {
        // Handle successful login, e.g., redirect to dashboard
        window.location.href = '/dashboard.html';
    })
    .catch(error => {
        console.error('Error during Google authentication:', error);
    });
    */
}

// Initialize Facebook SDK
window.fbAsyncInit = function() {
    FB.init({
        appId      : 'YOUR_FACEBOOK_APP_ID',
        cookie     : true,
        xfbml      : true,
        version    : 'v18.0'
    });
};

// Add Facebook SDK script
(function(d, s, id) {
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) return;
    js = d.createElement(s); js.id = id;
    js.src = "https://connect.facebook.net/en_US/sdk.js";
    fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));

// Facebook login status handler
function checkFacebookLoginState() {
    FB.getLoginStatus(function(response) {
        if (response.status === 'connected') {
            const accessToken = response.authResponse.accessToken;
            console.log("Facebook Access Token:", accessToken);
            
            // Send to your server for verification
            // Similar fetch call as with Google
        }
    });
}
