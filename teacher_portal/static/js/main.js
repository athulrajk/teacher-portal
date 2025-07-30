/**
 * Teacher Portal JS
 * Handles modal operations, form submissions, dropdown logic, and student management
 */
document.addEventListener('DOMContentLoaded', () => {
  const modal = document.getElementById('modal');
  const addBtn = document.getElementById('addBtn');
  const closeModal = document.getElementById('closeModal');
  const submitBtn = document.getElementById('submitStudent');

  // Open modal for adding a new student
  addBtn.onclick = () => {
    resetModal();
    modal.classList.remove('hidden');
  };

  // Close modal
  closeModal.onclick = () => modal.classList.add('hidden');

  // Submit add/edit student form
  submitBtn.onclick = () => {
    const id = document.getElementById('studentId').value;
    const name = document.getElementById('name').value.trim();
    const subject = document.getElementById('subject').value.trim();
    const marks = document.getElementById('marks').value.trim();

    // Validation
    if (!name || !subject || marks === '') {
      return alert('All fields are required');
    }
    if (isNaN(marks) || parseInt(marks) < 0) {
      return alert('Marks must be a non-negative number');
    }

    const url = id ? '/update_student/' : '/add_student/';
    const data = `name=${encodeURIComponent(name)}&subject=${encodeURIComponent(subject)}&marks=${marks}${id ? '&id=' + id : ''}`;

    // AJAX request to backend
    fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-CSRFToken': csrfToken,
      },
      body: data
    })
      .then(res => res.json())
      .then(data => {
        if (data.success) {
          location.reload();
        } else {
          alert("Something went wrong while saving the student.");
        }
      });
  };

  // Close dropdowns when clicking elsewhere
  document.addEventListener('click', () => {
    document.querySelectorAll('.dropdown').forEach(d => d.classList.remove('open'));
  });
});

/**
 * Toggle visibility of dropdown menu for a student row.
 * Adds 'drop-up' class if not enough space below.
 */
function toggleDropdown(event, id) {
  event.stopPropagation();

  // Close other dropdowns
  document.querySelectorAll('.dropdown').forEach(d => d.classList.remove('open'));
  document.querySelectorAll('.dropdown-menu').forEach(m => m.classList.remove('drop-up'));

  const dropdown = document.getElementById(`dropdown-${id}`);
  const menu = dropdown.querySelector('.dropdown-menu');
  dropdown.classList.add('open');

  // Temporarily show the menu to calculate position
  menu.style.visibility = 'hidden';
  menu.style.display = 'block';

  const menuRect = menu.getBoundingClientRect();
  const spaceBelow = window.innerHeight - menuRect.bottom;
  const spaceAbove = menuRect.top;

  // If insufficient space below, show upward
  if (spaceBelow < 160 && spaceAbove > 160) {
    menu.classList.add('drop-up');
  }

  // Reset visibility
  menu.style.visibility = '';
  menu.style.display = '';
}

/**
 * Populate the modal with existing student data for editing.
 */
function openEditModal(id, name, subject, marks) {
  document.getElementById('modal').classList.remove('hidden');
  document.getElementById('modalTitle').innerText = "Edit Student";
  document.getElementById('studentId').value = id;
  document.getElementById('name').value = name;
  document.getElementById('subject').value = subject;
  document.getElementById('marks').value = marks;
}

/**
 * Confirm and delete student by ID.
 */
function deleteStudent(id) {
  if (confirm("Are you sure you want to delete this student?")) {
    fetch(`/delete_student/${id}/`, {
      method: 'POST',
      headers: {
        'X-CSRFToken': csrfToken
      }
    })
      .then(res => res.json())
      .then(data => {
        if (data.success) {
          location.reload();
        } else {
          alert("Failed to delete student.");
        }
      });
  }
}

/**
 * Reset modal fields and title to default (add mode).
 */
function resetModal() {
  document.getElementById('modalTitle').innerText = "Add Student";
  document.getElementById('studentId').value = '';
  document.getElementById('name').value = '';
  document.getElementById('subject').value = '';
  document.getElementById('marks').value = '';
}
