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
});


/*-----------------------------------------------Freelance Dashboard-------------------------------------------------------------*/ 
  // Sample data for the performance chart
  const overviewData = [20, 100, 45, 60, 40, 50, 35];

  // Generate the chart bars
  const chartContainer = document.getElementById('overviewChart');
  
  if (chartContainer) {
      overviewData.forEach(value => {
          const bar = document.createElement('div');
          bar.className = 'chart-bar';
          bar.style.height = `${value}%`;
          chartContainer.appendChild(bar);
      });
  } else {
      console.error('Chart container not found');
  }





/*-------------------------------------Browse Tasks Listing and Filtering-------------------------------------------------------------*/ 
const allTasks = [
   {
      title: "Build a Portfolio Website",
      category: "Web Development",
      budget: 200,
      duration: "1 Week",
      description: "Looking for a web developer to build a responsive portfolio website using HTML, CSS, and JavaScript.",
      tags: ["HTML", "CSS", "JavaScript"]
  },
  {
      title: "Translate English to Spanish",
      category: "Writing & Translation",
      budget: 100,
      duration: "2 Days",
      description: "Need someone fluent in Spanish to translate documents from English to Spanish.",
      tags: ["Translation", "Spanish"]
  },
  {
      title: "Logo Design for Startup",
      category: "Design & Creative",
      budget: 150,
      duration: "3 Days",
      description: "Creative logo designer needed for a new tech startup.",
      tags: ["Logo Design", "Branding"]
  },
  {
      title: "Data Entry Assistant",
      category: "Admin Support",
      budget: 80,
      duration: "5 Days",
      description: "Looking for someone to help with data entry tasks including spreadsheets and organizing files.",
      tags: ["Excel", "Data Entry"]
  }
];

function renderTasks(tasks) {
  const container = document.getElementById('tasksContainer');
  if (!container) return;
  container.innerHTML = '';

  if (tasks.length === 0) {
      container.innerHTML = '<p>No tasks found.</p>';
      return;
  }

  tasks.forEach(task => {
      container.innerHTML += `
          <div class="card task-card p-3">
              <div class="d-flex justify-content-between">
                  <h5>${task.title}</h5>
                  <span class="badge bg-secondary">${task.category}</span>
              </div>
              <p class="text-muted">$${task.budget} • ${task.duration}</p>
              <p>${task.description}</p>
              <div class="mb-2">
                  ${task.tags.map(tag => `<span class="tag">${tag}</span>`).join('')}
              </div>
              <button class="btn btn-dark">Apply for Task</button>
          </div>
      `;
  });
}

function filterTasks() {
  const searchInput = document.getElementById('searchInput');
  const categoryFilter = document.getElementById('categoryFilter');
  
  const search = searchInput ? searchInput.value.toLowerCase() : '';
  const category = categoryFilter ? categoryFilter.value : '';
  
  const filtered = allTasks.filter(task => {
      const matchCategory = !category || task.category === category;
      const matchSearch = task.title.toLowerCase().includes(search) || task.description.toLowerCase().includes(search);
      return matchCategory && matchSearch;
  });
  renderTasks(filtered);
}

// Initialize tasks
renderTasks(allTasks);

// Set up event listeners for task filtering
const searchForm = document.getElementById('searchForm');
if (searchForm) {
  searchForm.addEventListener('submit', (e) => {
      e.preventDefault();
      filterTasks();
  });
}

const categoryFilter = document.getElementById('categoryFilter');
if (categoryFilter) {
  categoryFilter.addEventListener('change', () => {
      filterTasks();
  });
}

 /*-----------------------------------------------Post Task Form-------------------------------------------------------------*/ 


 const taskForm = document.getElementById('taskForm');
 if (taskForm) {
     taskForm.addEventListener('submit', function(e) {
         e.preventDefault();
         
         const titleInput = document.getElementById('title');
         const categoryInput = document.getElementById('category');
         const descriptionInput = document.getElementById('description');
         const budgetInput = document.getElementById('budget');
         const deadlineInput = document.getElementById('deadline');
         const skillsInput = document.getElementById('skills');
         
         if (titleInput && categoryInput && descriptionInput && budgetInput && deadlineInput && skillsInput) {
             const taskData = {
                 title: titleInput.value,
                 category: categoryInput.value,
                 description: descriptionInput.value,
                 budget: budgetInput.value,
                 deadline: deadlineInput.value,
                 skills: skillsInput.value.split(',').map(skill => skill.trim()),
             };
             
             console.log('Task Posted:', taskData);
             alert('Task has been posted!');
             this.reset();
             
             // You could add the new task to allTasks array and re-render here
             // Example:
             // allTasks.push({...taskData, tags: taskData.skills, duration: taskData.deadline});
             // renderTasks(allTasks);
         } else {
             console.error('One or more form elements could not be found');
         }
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