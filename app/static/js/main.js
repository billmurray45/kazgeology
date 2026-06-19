document.addEventListener("DOMContentLoaded", () => {
    // ── Hero Slider ──────────────────────────────────────────────
    const heroSection = document.querySelector('.hero');
    if (heroSection) {
        const indicators = document.querySelectorAll('.indicator');
        const captionElement = document.querySelector('.hero-caption');
        const slideData = [
            { img: 'https://kazgeology.kz/wp-content/uploads/2020/07/%D0%A3%D1%81%D1%82%D1%8E%D1%80%D1%82-%D0%9A%D0%97-1-1-1.png', caption: 'Устюрт, Казахстан' },
            { img: 'https://kazgeology.kz/wp-content/uploads/2020/07/3.jpg', caption: 'Промышленные объекты, Казахстан' },
            { img: 'https://images.unsplash.com/photo-1504307651254-35680f356f27?auto=format&fit=crop&q=80&w=2000', caption: 'Современные технологии разведки' }
        ];
        slideData.forEach(s => { const i = new Image(); i.src = s.img; });
        indicators.forEach((indicator, index) => {
            indicator.addEventListener('click', () => {
                indicators.forEach(ind => ind.classList.remove('active'));
                indicator.classList.add('active');
                heroSection.style.transition = 'background-image 0.4s ease-in-out';
                heroSection.style.backgroundImage = `url('${slideData[index].img}')`;
                if (captionElement) captionElement.textContent = slideData[index].caption;
            });
        });
    }

    // ── Video Click ──────────────────────────────────────────────
    const videoCard = document.getElementById('heroVideoCard');
    if (videoCard) {
        videoCard.addEventListener('click', function () {
            this.innerHTML = '<iframe src="https://www.youtube.com/embed/8aKDLubAV9M?start=4&autoplay=1" title="YouTube video" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>';
            this.style.backgroundImage = 'none';
            this.style.cursor = 'default';
        }, { once: true });
    }

    // ── Board Members Slider ─────────────────────────────────────
    const thumbs = document.querySelectorAll('.board-thumb');
    const track = document.getElementById('board-track');
    const mainImg = document.getElementById('board-main-img');
    const boardName = document.getElementById('board-name');
    const boardRole = document.getElementById('board-role');
    const boardSocial = document.getElementById('board-social');
    const boardDesc = document.getElementById('board-desc');
    const boardCurrent = document.getElementById('board-current');
    const boardTotal = document.getElementById('board-total');
    const btnPrev = document.getElementById('board-prev');
    const btnNext = document.getElementById('board-next');

    if (!thumbs.length || !track) return;

    const VISIBLE = 4;
    const GAP = 16;
    let activeIndex = 0;
    let trackOffset = 0;

    if (boardTotal) boardTotal.textContent = String(thumbs.length).padStart(2, '0');
    mainImg.style.transition = 'opacity 0.3s ease, transform 0.3s ease';

    function slideTrack(offset) {
        const tw = thumbs[0].offsetWidth + GAP;
        track.style.transform = `translateX(${-offset * tw}px)`;
    }

    function selectMember(index) {
        if (index < 0) index = thumbs.length - 1;
        if (index >= thumbs.length) index = 0;
        activeIndex = index;

        if (activeIndex < trackOffset) {
            trackOffset = activeIndex;
        } else if (activeIndex >= trackOffset + VISIBLE) {
            trackOffset = activeIndex - VISIBLE + 1;
        }
        slideTrack(trackOffset);

        thumbs.forEach(t => t.classList.remove('active'));
        thumbs[activeIndex].classList.add('active');

        mainImg.style.opacity = '0';
        mainImg.style.transform = 'scale(0.97)';
        setTimeout(() => {
            mainImg.src = thumbs[activeIndex].dataset.img;
            const show = () => { mainImg.style.opacity = '1'; mainImg.style.transform = 'scale(1)'; };
            mainImg.onload = show;
            if (mainImg.complete) show();
        }, 220);

        boardName.textContent = thumbs[activeIndex].dataset.name;
        boardRole.textContent = thumbs[activeIndex].dataset.role;
        boardSocial.textContent = thumbs[activeIndex].dataset.social;
        boardDesc.textContent = thumbs[activeIndex].dataset.desc;
        boardCurrent.textContent = String(activeIndex + 1).padStart(2, '0');
    }

    thumbs.forEach((t, i) => t.addEventListener('click', () => selectMember(i)));
    btnPrev.addEventListener('click', () => selectMember(activeIndex - 1));
    btnNext.addEventListener('click', () => selectMember(activeIndex + 1));
});
