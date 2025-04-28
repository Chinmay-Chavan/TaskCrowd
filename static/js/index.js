// Wait for DOM to be fully loaded before manipulating elements
document.addEventListener('DOMContentLoaded', function() {

  /*-------------------------Navbar buttons-------------------------------------------*/
  const nav1 = document.querySelector('#login');
  if (nav1) {
      nav1.addEventListener('click', function() {
          window.location.href='login.html';
      });
  }

  const nav2 = document.querySelector('#register');
  if (nav2) {
      nav2.addEventListener('click', function() {
          window.location.href='register.html';
      });
  }

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
          window.location.href='register.html';
      });
  }

  const secondaryButton = document.querySelector('.secondary');
  if (secondaryButton) {
      secondaryButton.addEventListener('click', function() {
          alert('Navigate to About Us Page');
          window.location.href='about.html';
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
/*------------------------------------------------------register-alert---------------------------------------------------------------------*/



  // Initialize particles.js
  particlesJS("particles-js", {
    "particles": {
        "number": {
            "value": 80,
            "density": {
                "enable": true,
                "value_area": 800
            }
        },
        "color": {
            "value": "#ffffff"
        },
        "shape": {
            "type": "circle",
            "stroke": {
                "width": 0,
                "color": "#000000"
            },
            "polygon": {
                "nb_sides": 5
            }
        },
        "opacity": {
            "value": 0.5,
            "random": false,
            "anim": {
                "enable": false,
                "speed": 1,
                "opacity_min": 0.1,
                "sync": false
            }
        },
        "size": {
            "value": 3,
            "random": true,
            "anim": {
                "enable": false,
                "speed": 40,
                "size_min": 0.1,
                "sync": false
            }
        },
        "line_linked": {
            "enable": true,
            "distance": 150,
            "color": "#ffffff",
            "opacity": 0.4,
            "width": 1
        },
        "move": {
            "enable": true,
            "speed": 6,
            "direction": "none",
            "random": false,
            "straight": false,
            "out_mode": "out",
            "bounce": false,
            "attract": {
                "enable": false,
                "rotateX": 600,
                "rotateY": 1200
            }
        }
    },
    "interactivity": {
        "detect_on": "window",
        "events": {
            "onhover": {
                "enable": true,
                "mode": "repulse"
            },
            "onclick": {
                "enable": true,
                "mode": "push"
            },
            "resize": true
        },
        "modes": {
            "grab": {
                "distance": 400,
                "line_linked": {
                    "opacity": 1
                }
            },
            "bubble": {
                "distance": 400,
                "size": 40,
                "duration": 2,
                "opacity": 8,
                "speed": 3
            },
            "repulse": {
                "distance": 200,
                "duration": 0.4
            },
            "push": {
                "particles_nb": 4
            },
            "remove": {
                "particles_nb": 2
            }
        }
    },
    "retina_detect": true
});



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
=======
const message = document.body.dataset.message;
if (message && message.trim() !== "") {
  alert(message); // Show alert

}


/*-----------------------------------------------Login-alert---------------------------------------------------------------------*/


const message1 = document.body.dataset.message1;
if (message1 && message1.trim() !== "") {
    alert(message1); // Show alert
}
  /*----------------------------Login with google--------------------------------------------*/                 
// Function for business Google Sign-In
window.handleBusinessGoogleSignIn = function(response) {
    // Get the ID token from the response
    const idToken = response.credential;
    console.log("Business Google Sign-In, ID Token:", idToken);
    
    // Send the token to your backend
    fetch('/auth/google/business', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ token: idToken })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Authentication failed');
        }
        return response.json();
    })
    .then(data => {
        // Save the token to localStorage for future API calls
        localStorage.setItem('access_token', data.access_token);
        // Only redirect after successful authentication
        window.location.href = 'Business_Dashboard.html';
    })
    .catch(error => {
        console.error('Error during Google authentication:', error);
        alert('Authentication failed. Please try again.');
    });
}

// Function for freelancer Google Sign-In
window.handleFreelancerGoogleSignIn = function(response) {
    const idToken = response.credential;
    console.log("Freelancer Google Sign-In, ID Token:", idToken);
    
    // Send the token to your backend
    fetch('/auth/google/freelancer', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ token: idToken })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Authentication failed');
        }
        return response.json();
    })
    .then(data => {
        // Save the token to localStorage for future API calls
        localStorage.setItem('access_token', data.access_token);
        // Only redirect after successful authentication
        window.location.href = 'Freelancer_Dashboard.html';
    })
    .catch(error => {
        console.error('Error during Google authentication:', error);
        alert('Authentication failed. Please try again.');
    });
}
/*-----------------------------------------------Logout---------------------------------------------------------------------*/
// Add this function to your JS
function signOutGoogle() {
    // Clear your application's session/token
    document.cookie = "access_token=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
    
    // Clear Google's session
    google.accounts.id.disableAutoSelect();
    
    // Optional: Revoke Google's token
    if (google.accounts.oauth2) {
        google.accounts.oauth2.revoke(googleToken, () => {
            console.log('Google token revoked');
        });
    }
}

/*-----------------------------------------------Business Dashboard-------------------------------------------------------------*/ 
 



/*-----------------------------------------------Freelance Dashboard-------------------------------------------------------------*/ 
  
  

 /*-----------------------------------------------Post Task Form-------------------------------------------------------------*/ 


 // ============ POST TASK LOGIC (for post_task.html) =============


const taskForm = document.getElementById('taskForm');
if (taskForm) {
    taskForm.addEventListener('submit', function (e) {
        e.preventDefault();


        // Get form values
        const title = document.getElementById('title').value.trim();
        const category = document.getElementById('category').value.trim();
        const description = document.getElementById('description').value.trim();
        const budget = document.getElementById('budget').value.trim();
        const deadline = document.getElementById('deadline').value.trim();
        const skills = document.getElementById('skills').value.trim();
        const fileInput = document.getElementById('fileInput');
        const file = fileInput ? fileInput.files[0] : null;

        // Validate fields
        if (!title || !category || !description || !budget || !deadline || !skills) {
            alert('Please fill in all fields.');
            return;
        }

        // Prepare form data
        const formData = new FormData();
        formData.append('title', title);
        formData.append('category', category);
        formData.append('description', description);
        formData.append('budget', budget);
        formData.append('deadline', deadline);
        formData.append('skills', skills);
        if (file) {
            formData.append('file', file);
        }

        // Send data to /post-task endpoint
        fetch('/post-task', {
            method: 'POST',
            body: formData
        })
        .then(response => {
            if (response.redirected) {
                window.location.href = response.url;
            } else {
                return response.text().then(text => {
                    console.error("Post failed:", text);
                    alert("There was an error posting your task.");
                });
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('There was an error posting your task.');
        });

       

    });
}

// ============ BROWSE TASK LOGIC (for browse_task.html) ============

const searchInput = document.getElementById('searchInput');
const categoryFilter = document.getElementById('categoryFilter');
const tasksContainer = document.getElementById('tasksContainer');

let allTasks = [];

// Function to render tasks to the page
function renderTasks(filter = {}) {
    const { search = '', category = '' } = filter;

    if (!tasksContainer) return;
    tasksContainer.innerHTML = '';  // Clear the container before re-rendering

    const filteredTasks = allTasks.filter(task => {
        const matchesSearch = task.title.toLowerCase().includes(search.toLowerCase()) ||
                              task.description.toLowerCase().includes(search.toLowerCase());
        const matchesCategory = !category || task.category === category;
        return matchesSearch && matchesCategory;
    });

    if (filteredTasks.length === 0) {
        tasksContainer.innerHTML = '<p class="text-muted">No matching tasks.</p>';
        return;
    }

    filteredTasks.forEach(task => {
        const fileLink = task.file_path ? `
            <a href="/static/uploaded_files/${task.file_path}" download class="btn btn-sm btn-outline-primary mb-2">
                Download File
            </a>` : '';

        const taskHTML = `
            <div class="card task-card p-3 mb-3">
                <div class="d-flex justify-content-between">
                    <h5>${task.title}</h5>
                    <span class="badge bg-secondary">${task.category}</span>
                </div>
                <p><strong>Budget:</strong> ₹${task.budget}</p>
                <p><strong>Deadline:</strong> ${task.deadline}</p>
                <p>${task.description}</p>
                <div class="mb-2">
                    ${task.skills.map(skill => `<span class="tag">${skill}</span>`).join(' ')}
                </div>
                ${fileLink}
                <form action="/applications/apply/${task.id}" method="POST" class="apply-task-form">
                   <button type="submit" class="btn btn-dark apply-task-btn">Apply for Task</button>
                </form>
            </div>
        `;
        tasksContainer.innerHTML += taskHTML;  // Add the task to the container
    });
    
    // Attach event listeners to apply buttons after they've been added to the DOM
    attachApplyButtonListeners();
}

// Function to attach event listeners to apply buttons
function attachApplyButtonListeners() {
    document.querySelectorAll('.apply-task-btn').forEach(button => {
        button.addEventListener('click', function() {
            const taskId = this.getAttribute('data-task-id');
            applyForTask(taskId);
        });
    });
}

function applyForTask(taskId) {
    console.log("TaskId received:", taskId);

    if (taskId === undefined) {
        alert("Invalid task ID.");
        return;
    }

    fetch('/applications/apply/' + taskId, {
        method: 'POST',
        credentials: 'include'  // Include cookies for authentication
    })
    .then(async response => {
        // Read the response as text first
        const responseText = await response.text();
        
        // Try to parse as JSON
        let data;
        try {
            data = JSON.parse(responseText);
        } catch (e) {
            // If not valid JSON, use the text directly
            data = { error: responseText };
        }

        if (response.ok) {
            //alert('Application submitted successfully!');
            window.location.href = '/Browse_Task.html';
        } else {
            console.error('Server Error:', data);

            // Display the error message from the server as an alert
            if (data && data.error) {
                alert(data.error);
                
                // Handle redirects based on status codes
                if (response.status === 401) {
                    window.location.href = '/login.html';
                } else {
                    // For other errors like "already applied", go back to the task list
                    window.location.href = '/Browse_Task.html';
                }
            } 
        }
    })
    .catch(error => {
        console.error("Error applying for task:", error);
        alert("There was an error applying for this task. Please try again.");
    });
}

// Fetch tasks from the backend API and render them
if (tasksContainer) {
    fetch('/api/tasks')
        .then(res => res.json())
        .then(data => {
            allTasks = data;
            renderTasks();  // Render the tasks once data is loaded
        })
        .catch(err => {
            console.error("Failed to fetch tasks:", err);
            tasksContainer.innerHTML = '<p class="text-danger">Failed to load tasks.</p>';
        });

    // Event listener for search input
    if (searchInput) {
        searchInput.addEventListener('input', () => {
            renderTasks({ search: searchInput.value, category: categoryFilter?.value });
        });
    }

    // Event listener for category filter change
    if (categoryFilter) {
        categoryFilter.addEventListener('change', () => {
            renderTasks({ search: searchInput?.value, category: categoryFilter.value });
        });
    }
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




/*------------------------------------------------------register-popup---------------------------------------------------------------------*/

  const message = document.body.dataset.message;
  if (message && message.trim() !== "") {
    alert(message); // Show alert
  }


/*-----------------------------------------------Login-popup---------------------------------------------------------------------*/

  
  const message1 = document.body.dataset.message;
  if (message1 && message.trim() !== "") {
      alert(message); // You can style this later or use a toast instead
  }


/*Toast message for invalid credentials-----------------------*/
function showToast(message) {
  const toast = document.getElementById("toast");
  if (!toast) return;

  toast.textContent = message;
  toast.classList.remove("hidden");
  toast.classList.add("show");

  setTimeout(() => {
    toast.classList.remove("show");
    toast.classList.add("hidden");
  }, 4000);
}


/*---------------------------------------------------------------------------------------------------------------------------------- */

/*-----------------------------------------------------Submit Work-------------------------------------------------------------------- */











});



