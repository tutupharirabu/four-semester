/* Membuat variabel text, leaf, hill1, hill4, dan hill5 
yang mereferensikan elemen HTML dengan ID yang sesuai. */
let text = document.getElementById('text');
let leaf = document.getElementById('leaf');
let hill1 = document.getElementById('hill1');
let hill4 = document.getElementById('hill4');
let hill5 = document.getElementById('hill5');

/* Menambahkan event listener pada objek window untuk mendengarkan mengecek scroll */
window.addEventListener('scroll', () => {
    let value = window.scrollY; 

    /* Mengubah properti gaya CSS dari elemen-elemen yang 
    dipilih berdasarkan nilai scroll (value) */
    text.style.marginTop = value * 2.5 + 'px';
    leaf.style.top = value * -1.5 + 'px';
    leaf.style.left = value * 1.5 + 'px';
    hill5.style.left = value * 1.5 + 'px';
    hill4.style.left = value * -1.5 + 'px';
    hill1.style.top = value * 1 + 'px';
})