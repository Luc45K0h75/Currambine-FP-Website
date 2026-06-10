// Filter team by category
function filterTeam(categoryId, btn) {
    document.querySelectorAll('.team-filter .btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');

    document.querySelectorAll('.team-card-col').forEach(card => {
        card.style.display = (categoryId === 'all' || card.dataset.category === categoryId) ? 'block' : 'none';
    });

    document.querySelectorAll('.team-category').forEach(section => {
        if (categoryId === 'all') {
            section.style.display = 'block';
        } else {
            const hasVisible = Array.from(section.querySelectorAll('.team-card-col'))
                .some(card => card.dataset.category === categoryId);
            section.style.display = hasVisible ? 'block' : 'none';
        }
    });
}

// Populate bio modal
document.getElementById('bioModal').addEventListener('show.bs.modal', function(event) {
    const btn = event.relatedTarget;
    const photoUrl = btn.dataset.photo;
    const quals = btn.dataset.quals;
    const bio = btn.dataset.bio;

    document.getElementById('modalName').textContent = btn.dataset.name;
    document.getElementById('modalType').textContent = btn.dataset.type;

    const bioEl = document.getElementById('modalBio');
    if (quals) {
        bioEl.innerHTML = '<strong>' + quals + '</strong><br><br>' + bio;
    } else {
        bioEl.textContent = bio;
    }

    const photoEl = document.getElementById('modalPhoto');
    if (photoUrl) {
        photoEl.src = '/static/images/team/' + photoUrl;
        photoEl.style.display = 'block';
        document.querySelector('.bio-modal-photo-col').style.display = 'block';
        document.querySelector('#bioModal .col-md-8').className = 'col-md-8 bio-modal-text';
    } else {
        photoEl.style.display = 'none';
        document.querySelector('.bio-modal-photo-col').style.display = 'none';
        document.querySelector('#bioModal .col-md-8').className = 'col-12 bio-modal-text';
    }
});