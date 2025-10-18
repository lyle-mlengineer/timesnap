const extractForm = document.getElementById('extract-form')

extractForm.addEventListener('submit', (e) => {
    e.preventDefault()
    const results = document.querySelector('.result')
    results.innerHTML = ''
    const form = new FormData(extractForm)
    fetch('/extract', {
        method: 'POST',
        body: form
    })
    .then(res => res.json())
    .then(res => {
        results.style.backgroundColor = res.style_bg_color
        results.innerHTML = res.highlighted_code
        document.head.innerHTML += res.style_definitions
        results.style.height = `min(calc(${res.num_lines}em * 1.5 + 2 * 1em), 25em)`
        results.style.display = 'block'
    })
    .catch(err => console.log(err))
    })

// extractForm.addEventListener('submit', (e) => {
//     e.preventDefault()
//     const results = document.querySelector('.result')
//     results.innerHTML = ''
//     const form = new FormData(extractForm)
//     fetch('/extract', {
//         method: 'POST',
//         body: form
//     })
//     .then(res => res.json())
//     .then(res => {
//         const downloadLink = document.getElementById('action-download')
//         downloadLink.href = res.file_path._url
//         results.style.backgroundColor = res.style_bg_color
//         results.innerHTML = res.highlighted_code
//         document.head.innerHTML += res.style_definitions
//         results.style.height = `min(calc(${res.num_lines}em * 1.5 + 2 * 1em), 25em)`

//         const styleSelector = document.getElementById('style')
//         styleSelector.innerHTML = ''
//         res.all_styles.forEach(style => {
//             const option = document.createElement('option')
//             option.value = style
//             option.innerText = style
//             styleSelector.appendChild(option)
//             if (style === res.style) {
//                 option.selected = true
//             }
//         })

//         results.style.display = 'block'
//     })
//     .catch(err => console.log(err))
// })
