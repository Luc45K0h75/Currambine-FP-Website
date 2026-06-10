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

    document.getElementById('modalName').textContent = btn.dataset.name;
    document.getElementById('modalType').textContent = btn.dataset.type;
    document.getElementById('modalQuals').textContent = btn.dataset.quals;
    document.getElementById('modalBio').textContent = btn.dataset.bio;

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