// Wait for DOM to be fully loaded before manipulating elements
document.addEventListener('DOMContentLoaded', function() {

  /*-------------------------Sidebar-------------------------------------------*/
  window.openSidebar = function() { 
      document.getElementById("sidebar").style.width = "250px";
  }

  window.closeSidebar = function() {
      document.getElementById("sidebar").style.width = "0";
  }

  /*-------------------------Hero section-------------------------------------------*/
  const primaryButton = document.querySelector('.primary');
  if (primaryButton) {
      primaryButton.addEventListener('click', function() {
          alert('Navigate to Registration Page');
      });
  }

  const secondaryButton = document.querySelector('.secondary');
  if (secondaryButton) {
      secondaryButton.addEventListener('click', function() {
          alert('Navigate to About Us Page');
      });
  }

  const btp = document.querySelector('.cd-1');
  if (btp) {
     btp.addEventListener('click', function() {
          alert('Navigate to Register Page');
          window.location.href='register.html';
      });
  }

  const btp2 = document.querySelector('.cd-2');
  if (btp2) {
     btp2.addEventListener('click', function() {
          alert('Navigate to Register Page');
          window.location.href='register.html';
      });
  }

  const btp3 = document.querySelector('.cd-3');
  if (btp3) {
     btp3.addEventListener('click', function() {
          alert('Navigate to About Us Page');
          window.location.href='about.html';
      });
  }

  /*----------------------------Login form AND Register form---------------------------------------------*/ 
  
  window.openForm = function(formId) {
      // Get all elements with class 'form-popup-R'
      let forms = document.getElementsByClassName('form-popup');

      // Loop through each form and hide it
      for (let i = 0; i < forms.length; i++) {
          forms[i].style.display = 'none';
      }

      // Show the selected form
      document.getElementById(formId).style.display = 'block';
  }

  /*----------------------------Login with google--------------------------------------------*/                 
  // Function for business Google Sign-In
window.handleBusinessGoogleSignIn = function(response) {
  // Get the ID token from the response
  const idToken = response.credential;
  console.log("Business Google Sign-In, ID Token:", idToken);
  
  // Redirect to business dashboard
  window.location.href = 'Business_Dashboard.html';
  
  /* When you add backend validation:
  fetch('/auth/google/business', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({ token: idToken })
  })
  .then(response => response.json())
  .then(data => {
      window.location.href = 'http://localhost:5500/Business_Dashboard.html';
  })
  .catch(error => {
      console.error('Error during Google authentication:', error);
  });
  */
}
// Function for freelancer Google Sign-In
window.handleFreelancerGoogleSignIn = function(response) {
  const idToken = response.credential;
  console.log("Freelancer Google Sign-In, ID Token:", idToken);
  window.location.href = 'http://localhost:5500/Freelancer_Dashboard.html';
}

// Function for admin Google Sign-In
window.handleAdminGoogleSignIn = function(response) {
  const idToken = response.credential;
  console.log("Admin Google Sign-In, ID Token:", idToken);
  window.location.href = 'http://localhost:5500/Admin_Dashboard.html';
}

/*------------------------------------------------------------------------------------------------*/



  // Add click event listeners to all Facebook login buttons
  const fbButtons = document.querySelectorAll('.fb-material-button');
  fbButtons.forEach(button => {
    button.addEventListener('click', function(event) {
      event.preventDefault();
      handleFacebookLogin();
    });
  });

  

/*----------------------------Facebook Login Integration--------------------------------------------*/
// Initialize the Facebook SDK
window.fbAsyncInit = function() {
  FB.init({
    appId      : '2300712287046729', // Replace with your actual Facebook App ID
    cookie     : true,
    xfbml      : true,
    version    : 'v18.0' // Use the latest version of the Graph API
  });
    
  // Check login status on page load (optional)
  FB.getLoginStatus(function(response) {
    statusChangeCallback(response);
  });
};

// Load the SDK asynchronously
(function(d, s, id) {
  var js, fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) return;
  js = d.createElement(s); js.id = id;
  js.src = "https://connect.facebook.net/en_US/sdk.js";
  fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));

// Handle the status change response
function statusChangeCallback(response) {
  if (response.status === 'connected') {
    // User is logged in and has authenticated your app
    console.log('Facebook login successful');
    getUserInfo();
  } else {
    console.log('User not authenticated with Facebook');
  }
}

// Get user information after successful login
function getUserInfo() {
  FB.api('/me', {fields: 'name,email'}, function(response) {
    console.log('User name: ' + response.name);
    console.log('User email: ' + response.email);
    
    // Here you can:
    // 1. Store user data in local storage/session
    // 2. Redirect to dashboard or home page
    // 3. Send data to your backend for authentication
  });
}

// Function to handle Facebook login button click
function handleFacebookLogin() {
  FB.login(function(response) {
    if (response.authResponse) {
      console.log('Facebook authentication successful');
      // Get access token
      const accessToken = response.authResponse.accessToken;
      const userID = response.authResponse.userID;
      
      // Log the token (for debugging purposes)
      console.log('Access Token:', accessToken);
      
      // You can send this token to your server
      // sendTokenToServer(accessToken, userID);
      
      // Get user info
      getUserInfo();
    } else {
      console.log('User cancelled login or did not fully authorize.');
    }
  }, {scope: 'public_profile,email'});
}

// Add this to your existing Facebook code
function checkLoginState() {
  FB.getLoginStatus(function(response) {
    console.log("FB login status:", response);
    statusChangeCallback(response);
  });
}

/*-----------------------------------------------Business Dashboard-------------------------------------------------------------*/ 
  // Sample data for the performance chart
  const performanceData = [20, 100, 45, 60, 40, 50, 35];

  // Generate the chart bars
  const chartContainer = document.getElementById('performanceChart');
  
  if (chartContainer) {
      performanceData.forEach(value => {
          const bar = document.createElement('div');
          bar.className = 'chart-bar';
          bar.style.height = `${value}%`;
          chartContainer.appendChild(bar);
      });
  } else {
      console.error('Chart container not found');
  }



/*-----------------------------------------------Freelance Dashboard-------------------------------------------------------------*/ 
  // Sample data for the performance chart
  const overviewData = [20, 100, 45, 60, 40, 50, 35];

  // Generate the chart bars
  const overviewChartContainer = document.getElementById('overviewChart');
  
  if (overviewChartContainer) {
      overviewData.forEach(value => {
          const bar = document.createElement('div');
          bar.className = 'chart-bar';
          bar.style.height = `${value}%`;
          overviewChartContainer.appendChild(bar);
      });
  } else {
      console.error('Chart container not found');
  }





/*-------------------------------------Browse Tasks Listing and Filtering-------------------------------------------------------------*/ 


// ============ BROWSE TASK LOGIC (for browse_task.html) ============

const searchInput = document.getElementById('searchInput');
const categoryFilter = document.getElementById('categoryFilter');
const tasksContainer = document.getElementById('tasksContainer');

function renderTasks(filter = {}) {
    const { search = '', category = '' } = filter;
    if (!tasksContainer) return;

    tasksContainer.innerHTML = '';
    const tasks = JSON.parse(localStorage.getItem('tasks')) || [];

    const filtered = tasks.filter(task => {
        const matchesSearch = task.title.toLowerCase().includes(search.toLowerCase()) ||
                              task.description.toLowerCase().includes(search.toLowerCase());
        const matchesCategory = !category || task.category === category;
        return matchesSearch && matchesCategory;
    });

    if (filtered.length === 0) {
        tasksContainer.innerHTML = '<p class="text-muted">No matching tasks.</p>';
        return;
    }

    filtered.forEach(task => {
        const taskHTML = `
            <div class="card task-card p-3 mb-3">
                <div class="d-flex justify-content-between">
                    <h5>${task.title}</h5>
                    <span class="badge bg-secondary">${task.category}</span>
                </div>
                <p class="text-muted">₹${task.budget} • ${task.deadline}</p>
                <p>${task.description}</p>
                <div class="mb-2">
                    ${task.skills.map(skill => `<span class="tag">${skill}</span>`).join('')}
                </div>
                <button class="btn btn-dark">Apply for Task</button>
            </div>
        `;
        tasksContainer.innerHTML += taskHTML;
    });
}

// If on browse page, auto-render tasks
if (tasksContainer) {
    renderTasks();

    if (searchInput) {
        searchInput.addEventListener('input', () => {
            renderTasks({ search: searchInput.value, category: categoryFilter.value });
        });
    }

    if (categoryFilter) {
        categoryFilter.addEventListener('change', () => {
            renderTasks({ search: searchInput.value, category: categoryFilter.value });
        });
    }
}



 /*-----------------------------------------------Post Task Form-------------------------------------------------------------*/ 


 // ============ POST TASK LOGIC (for post_task.html) =============

const taskForm = document.getElementById('taskForm');
if (taskForm) {
    taskForm.addEventListener('submit', function (e) {
        e.preventDefault();

        const title = document.getElementById('title').value;
        const category = document.getElementById('category').value;
        const description = document.getElementById('description').value;
        const budget = document.getElementById('budget').value;
        const deadline = document.getElementById('deadline').value;
        const skills = document.getElementById('skills').value.split(',').map(s => s.trim());

        const task = {
            title,
            category,
            description,
            budget,
            deadline,
            skills
        };

        let tasks = JSON.parse(localStorage.getItem('tasks')) || [];
        tasks.push(task);
        localStorage.setItem('tasks', JSON.stringify(tasks));

        alert('Task has been posted!');
        taskForm.reset();
    });
}




 /*------------------------------------------------------ Contact Us -----------------------------------------------------------------------*/

 document.getElementById('contactForm').addEventListener('submit', function(e) {
  e.preventDefault();
  
  // Get form values
  const name = document.getElementById('name').value;
  const email = document.getElementById('email').value;
  const subject = document.getElementById('subject').value;
  const message = document.getElementById('message').value;
  
  // Here you would typically send the data to your server
  // For this example, we'll just show a success message
  console.log('Form submitted:', { name, email, subject, message });
  
  // Show success message
  document.getElementById('successMessage').style.display = 'block';
  
  // Reset form
  document.getElementById('contactForm').reset();
  
  // Hide success message after 5 seconds
  setTimeout(function() {
      document.getElementById('successMessage').style.display = 'none';
  }, 2000);
});



/*------------------------------------------------------ Profile -----------------------------------------------------------------------*/


document.getElementById("uploadBtn").addEventListener("click", function () {
  const input = document.getElementById("imageInput");
  const file = input.files[0];

  if (file) {
    const reader = new FileReader();

    reader.onload = function (e) {
      const svgImage = document.getElementById("svgImage");
      svgImage.setAttribute("href", e.target.result);
    };

    reader.readAsDataURL(file);
  } else {
    alert("Please select an image file first.");
  }
});
});


/*------------------------------------------------------register-popup---------------------------------------------------------------------*/
window.addEventListener("DOMContentLoaded", function () {
  const message = document.body.dataset.message;
  if (message && message.trim() !== "") {
    alert(message); // Show alert
  }
});

/*-----------------------------------------------Login-popup---------------------------------------------------------------------*/

window.addEventListener("DOMContentLoaded", function () {
  const message = document.body.dataset.message;
  if (message && message.trim() !== "") {
      alert(message); // You can style this later or use a toast instead
  }
});


