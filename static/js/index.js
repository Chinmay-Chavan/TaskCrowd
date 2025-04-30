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



  


  /*----------------------------Login with google--------------------------------------------*/                 
  // Function for business Google Sign-In
/*window.handleBusinessGoogleSignIn = function(response) {
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
  
}
// Function for freelancer Google Sign-In
window.handleFreelancerGoogleSignIn = function(response) {
  const idToken = response.credential;
  console.log("Freelancer Google Sign-In, ID Token:", idToken);
  window.location.href = 'http://localhost:5500/Freelancer_Dashboard.html';

/*const message = document.body.dataset.message;
if (message && message.trim() !== "") {
  alert(message); // Show alert

}*/


/*-----------------------------------------------Login-alert---------------------------------------------------------------------*/


/*const message1 = document.body.dataset.message1;
if (message1 && message1.trim() !== "") {
    alert(message1); // Show alert
}*/
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
                <form action="/applications/apply/${ task.id }" method="POST" class="apply-task-form" id="data-task-id">
                   <input type="hidden" name="task_id" value="${ task.id }">
                   <button type="submit" class="btn btn-dark apply-task-btn">Apply for Task</button>
                </form>
            </div>
        `;
        tasksContainer.innerHTML += taskHTML;  // Add the task to the container
    });

    // Now attach event listeners to new buttons after rendering
    document.querySelectorAll('.apply-task-btn').forEach(button => {
        button.addEventListener('click', function() {
            const taskId = this.getAttribute('data-task-id');
            applyForTask(taskId);
        });
    });
}

// Function to get a cookie value by name
/*function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}
*/

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

//Business Dashboard Js
const businessTasksContainer = document.getElementById('businessTasksContainer');
    
    if (businessTasksContainer) {
        fetch('/api/business/tasks')
            .then(response => {
                if (!response.ok) {
                    if (response.status === 401) {
                        window.location.href = '/login.html';
                        return;
                    }
                    throw new Error('Server error');
                }
                return response.json();
            })
            .then(tasks => {
                if (tasks.length === 0) {
                    businessTasksContainer.innerHTML = '<p>You have not posted any tasks yet.</p>';
                    return;
                }
                
                tasks.forEach(task => {
                    const taskCard = `
                        <div class="card mb-3">
                            <div class="card-body">
                                <h5 class="card-title">${task.title}</h5>
                                <p class="card-text">${task.description}</p>
                                <p><strong>Budget:</strong> $${task.budget}</p>
                                <p><strong>Category:</strong> ${task.category}</p>
                                <p><strong>Deadline:</strong> ${task.deadline}</p>
                                <div class="d-flex justify-content-end">
                                    <button class="btn btn-primary me-2" onclick="editTask(${task.id})">
                                        Edit Task
                                    </button>
                                    <button class="btn btn-danger" onclick="deleteTask(${task.id})">
                                        Delete Task
                                    </button>
                                </div>
                            </div>
                        </div>
                    `;
                    businessTasksContainer.innerHTML += taskCard;
                });
            })
            .catch(error => {
                console.error('Error fetching tasks:', error);
                businessTasksContainer.innerHTML = '<p class="text-danger">Failed to load your tasks. Please try again later.</p>';
            });
    }


    //Freelancer Dashboard Js
    const availableTasksContainer = document.getElementById('availableTasksContainer');
    
    if (availableTasksContainer) {
            fetch('/api/freelancer/available-tasks')
            .then(response => {
                if (!response.ok) {
                    if (response.status === 401) {
                        window.location.href = '/login.html';
                        return;
                    }
                    throw new Error('Server error');
                }
                return response.json();
            })
            .then(tasks => {
                if (tasks.length === 0) {
                    availableTasksContainer.innerHTML = '<p>No tasks available at the moment.</p>';
                    return;
                }
                
                tasks.forEach(task => {
                    const taskCard = `
                        <div class="card mb-3">
                            <div class="card-body">
                                <h5 class="card-title">${task.title}</h5>
                                <p class="card-text">${task.description}</p>
                                <p><strong>Budget:</strong> $${task.budget}</p>
                                <p><strong>Category:</strong> ${task.category}</p>
                                <p><strong>Deadline:</strong> ${task.deadline}</p>
                                <div class="mb-2">
                                    ${task.skills.map(skill => `<span class="tag">${skill}</span>`).join(' ')}
                                </div>
                                <button class="btn btn-primary" onclick="applyToTask(${task.id})">
                                    Apply for Task
                                </button>
                            </div>
                        </div>
                    `;
                    availableTasksContainer.innerHTML += taskCard;
                });
            })
            .catch(error => {
                console.error('Error fetching tasks:', error);
                availableTasksContainer.innerHTML = '<p class="text-danger">Failed to load available tasks. Please try again later.</p>';
            });
    }



/*----------------------------Request page authentication with jwt ---------------------------------------------*/
// Function to get the JWT token from localStorage
function getAuthToken() {
    return localStorage.getItem('auth_token');
}

// Function to handle apply button clicks
async function handleApply(event) {
    const taskId = event.target.dataset.taskId;
    const token = getAuthToken();
    
    if (!token) {
        window.location.href = '/login?redirect=' + encodeURIComponent(window.location.pathname);
        return;
    }
    
    try {
        const response = await fetch(`/applications/apply/${taskId}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            }
        });
        
        if (response.status === 401) {
            alert('Your session has expired. Please log in again.');
            window.location.href = '/login?redirect=' + encodeURIComponent(window.location.pathname);
            return;
        }
        
        const result = await response.json();
        
        if (response.ok) {
            alert('Application submitted successfully!');
            event.target.disabled = true;
            event.target.textContent = 'Applied';
        } else {
            alert(`Error: ${result.detail || 'Could not submit application'}`);
        }
    } catch (error) {
        console.error('Error applying for task:', error);
        alert('Error submitting application. Please try again later.');
    }
}

// Function to load and render tasks
async function loadTasks() {
    const token = getAuthToken();
    const tasksContainer = document.getElementById('tasksContainer');
    
    try {
        const response = await fetch('/api/tasks', {
            headers: {
                'Authorization': token ? `Bearer ${token}` : ''
            }
        });
        
        if (response.status === 401) {
            console.log('Please log in to view all available tasks');
        }
        
        const tasks = await response.json();
        
        // Clear existing tasks
        tasksContainer.innerHTML = '';
        
        // Render each task
        tasks.forEach(task => {
            const taskCard = document.createElement('div');
            taskCard.className = 'card task-card mb-3';
            
            // Format the skills as tags
            const skillsHtml = task.skills
                .split(',')
                .map(skill => `<span class="tag">${skill.trim()}</span>`)
                .join(' ');
            
            taskCard.innerHTML = `
                <div class="card-body">
                    <h5 class="card-title">${task.title}</h5>
                    <p class="card-text">${task.description}</p>
                    <div class="d-flex justify-content-between align-items-center mb-2">
                        <span class="badge bg-primary">$${task.budget}</span>
                        <span class="text-muted">Deadline: ${task.deadline}</span>
                    </div>
                    <div class="mb-3">
                        <strong>Skills:</strong> ${skillsHtml}
                    </div>
                    <button class="btn btn-success apply-btn" data-task-id="${task.id}">Apply</button>
                </div>
            `;
            
            tasksContainer.appendChild(taskCard);
        });
        
        // Add event listeners to all Apply buttons
        document.querySelectorAll('.apply-btn').forEach(button => {
            button.addEventListener('click', handleApply);
        });
        
    } catch (error) {
        console.error('Error loading tasks:', error);
        tasksContainer.innerHTML = '<div class="alert alert-danger">Error loading tasks. Please try again later.</div>';
    }
}
    
    // Add search form functionality if needed
    const searchForm = document.getElementById('searchForm');
    if (searchForm) {
        searchForm.addEventListener('submit', function(e) {
            e.preventDefault();
            // Add your search logic here
            loadTasks(); // Reload tasks with filters
        });
    }



//----------------------------------------Request Page (Accepted/Rejected)--------------------------------------------------------------------------

// Object to track application statuses in the current session
const applicationStatuses = {};

// Initialize application statuses from the page data
document.addEventListener('DOMContentLoaded', function() {
    const cards = document.querySelectorAll('.card-rqequest');
    cards.forEach(card => {
        const appId = card.getAttribute('data-app-id');
        const status = card.getAttribute('data-status');
        if (appId) {
            applicationStatuses[appId] = status;
        }
    });
               
    // Add event listeners to all request forms
    const forms = document.querySelectorAll('.request-form');
    forms.forEach(form => {
        form.addEventListener('submit', handleRequestUpdate);
    });
});
           
function handleRequestUpdate(event) {
    event.preventDefault(); // Prevent default form submission
    
    const form = event.currentTarget;
    const appId = form.getAttribute('data-app-id');
    const statusInput = form.querySelector('input[name="status"]');
    const newStatus = statusInput.value;
               
    // Check if the application has already been processed
    if (applicationStatuses[appId] === 'accepted' && newStatus === 'accepted') {
        showAlert('This application has already been accepted.', false);
        return;
    }
               
    if (applicationStatuses[appId] === 'rejected' && newStatus === 'rejected') {
        showAlert('This application has already been rejected.', false);
        return;
    }
               
    // Fix #1: Update the form action URL to include the correct prefix
    // Make sure the form action is correctly set with the /applications prefix
    const url = `/applications/requests/${appId}/update`;
                   
    // Use fetch API to submit the form asynchronously
    fetch(url, {
        method: 'POST',
        body: new FormData(form),
        headers: {
            'X-Requested-With': 'XMLHttpRequest'
        }
    })
    .then(response => {
        if (response.ok) {
            return response.json(); // Parse JSON response
        } else {
            throw new Error('Network response was not ok');
        }
    })
    .then(data => {
        // Update our local tracking
        applicationStatuses[appId] = newStatus;
        // Update UI after successful response
        updateUI(appId, newStatus);
        showAlert(newStatus === 'accepted' ? 
            'Application successfully accepted!' : 
            'Application successfully rejected!', 
            true);
    })
    .catch(error => {
        console.error('Error:', error);
        showAlert('There was a problem updating the application status.', false);
    });
}
           
function updateUI(appId, status) {
    const card = document.querySelector(`.card-rqequest[data-app-id="${appId}"]`);
    if (!card) return;
               
    const actionButtons = card.querySelector('.action-buttons-rqequest');
    if (!actionButtons) return;
               
    // Update the UI based on new status
    if (status === 'accepted') {
        actionButtons.innerHTML = '<button class="btn-rqequest btn-accepted-rqequest" disabled>Accepted</button>';
        card.setAttribute('data-status', 'accepted');
    } else if (status === 'rejected') {
        actionButtons.innerHTML = '<button class="btn-rqequest btn-rejected-rqequest" disabled>Rejected</button>';
        card.setAttribute('data-status', 'rejected');
    }
}
           
function showAlert(message, isSuccess) {
    const alertContainer = document.getElementById('alertContainer');
    const alertMessage = document.getElementById('alertMessage');
    
    if (!alertContainer || !alertMessage) {
        alert(message); // Fallback if alert container doesn't exist
        return;
    }
               
    alertMessage.textContent = message;
    alertContainer.style.display = 'block';
               
    if (isSuccess) {
        alertContainer.classList.add('success');
        alertContainer.classList.remove('error');
    } else {
        alertContainer.classList.add('error');
        alertContainer.classList.remove('success');
    }
               
    // Auto-close after 5 seconds
    setTimeout(closeAlert, 5000);
}
           
function closeAlert() {
    const alertContainer = document.getElementById('alertContainer');
    if (alertContainer) {
        alertContainer.style.display = 'none';
    }
}
});