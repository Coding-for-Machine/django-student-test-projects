
const url = window.location.href;
const quizBox = document.getElementById('quiz-box');
const qcloseBox = document.getElementById('close-box');

const scoreBox = document.getElementById('scrore-box');
const resaultBox = document.getElementById('resault-box');
const TimerBox = document.getElementById('timer-box');
const closeBox = document.getElementById('close-box');


const startsTimer = (vaqti) => {
  console.log(vaqti)
  let minutes = vaqti - 1;
  let seconds = 60;
  let timer = setInterval(() => {
    seconds--;
    if (seconds < 0) {
      seconds = 59;
      minutes--;
    }
    TimerBox.innerHTML = `<br>${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}</br>`;
    if (minutes === 0 && seconds === 0) {
      TimerBox.innerHTML = `00:00`;
      let clearVaqt = setTimeout(() => {
        clearInterval(timer);
        clearTimeout(clearVaqt);
        alert('vaqt tugadi');
        sendData();
      }, 500);
    }
  }, 1000);
};


$.ajax({
  type: 'GET',
  url: `${url}api/quiz/`, // Ensure `url` is defined and ends with a `/`
  success: (response) => {
    const data = response.data; // Extract data from the response
    console.log(response.vaqti); // Logs the timer value
    
    data.forEach((element) => {
      const { text: questionText, varyants } = element; // Destructure question text and options
      
      // Add the question
      quizBox.innerHTML += `
        <article class="group m-4 flex rounded-md max-w-full flex-col overflow-hidden border border-neutral-300 bg-neutral-50 text-neutral-600 dark:border-neutral-700 dark:bg-neutral-900 dark:text-neutral-300">
            <div class="h-44 md:h-64 overflow-hidden"> 
                <img src="${element.image || 'https://penguinui.s3.amazonaws.com/component-assets/card-img-1.webp'}" 
                     class="object-cover transition duration-700 ease-out group-hover:scale-105" 
                     alt="Question Image" />
            </div>
            <div class="flex flex-col gap-4 p-6">
                <h3 class="text-balance text-xl lg:text-2xl font-bold text-neutral-900 dark:text-white" aria-describedby="featureDescription">
                    ${questionText}
                </h3>

            </div>
        </article>
      `;
      
      // Add the options
      varyants.forEach((option) => {
        quizBox.innerHTML += `
        <!-- Mac -->
        <label class="w-[96%] m-4 p-2 relative flex items-center gap-4 rounded-md bg-neutral-50  hover:scale-105 transition-transform text-neutral-600 dark:text-neutral-300 dark:bg-neutral-900 has-[:checked]:border-black has-[:checked]:bg-black/5 has-[:checked]:text-neutral-900 has-[:checked]:border has-[:checked]:border-primary has-[:focus]:outline has-[:focus]:outline-2 has-[:focus]:outline-offset-2 has-[:focus]:outline-black dark:has-[:checked]:border-white dark:has-[:checked]:text-white dark:has-[:checked]:bg-white/5 dark:has-[:focus]:outline-white border border-neutral-300 dark:border-neutral-700"
         for="${questionText}-${option.id}">
            <input type="radio"  class="ans" id="${questionText}-${option.id}" name="${questionText}" value="${option.text}" aria-describedby="macDescription"  checked />
            <div class="flex flex-col">
                <h3 class="font-medium" aria-hidden="true">${option.text}</h3>
            </div>
        </label>
        `;
      });

    });

    // Start the timer with the response value
    startsTimer(response.vaqti);
  },
  error: (error) => {
    console.error('Error fetching data:', error);
  }
});



const quizForm = document.getElementById("quiz-form");
const csrfToken = document.getElementsByName("csrfmiddlewaretoken")[0].value;

const sendData = () => {
  const elements = [...document.getElementsByClassName("ans")];
  const data = {};
  data['csrfmiddlewaretoken'] = csrfToken;
  elements.forEach((el) => {
    if (el.checked) {
      data[el.name] = el.value;
    } else {
      if (!data[el.name]) {
        data[el.name] = null;
      }
    }
  });
 

  $.ajax({
    type: `POST`,
    url: `${url}save/`,
    data: data,
    success: function(response){
        const resolt=response.results
        quizForm.classList.add('hidden')
        closeBox.classList.add('hidden')
        scoreBox.innerHTML=`${response.passed ? 'Congratulations ': 'Sizning Natijanggiz'} ${response.score.toFixed(2)}%`
        resolt.forEach(res=>{
            const resDev= document.createElement("div")
            for (const [question, resp] of Object.entries(res)){
                resDev.innerHTML+=question
                const cls=['p-3', 'text-center', 'text-sm',"w-96", "rounded-lg", "m-6", 'text-sm', 'text-rose-50' ]
                resDev.classList.add(...cls)
                if (resp=="javob berilmagan"){
                    resDev.innerHTML+="Javob berilmadi"
                    resDev.classList.add('bg-red-300')
                }else{
                    const answers=resp['nateja_a']
                    const natejs=resp['nateja']
                    if (answers==natejs){
                        resDev.classList.add("bg-blue-600")
                        resDev.innerHTML+=` To'g'ri Javob Berdinggiz  ${answers}`
                    }else{
                        resDev.classList.add("bg-red-700")
                        resDev.innerHTML +=`To'g'ri javob: ${natejs}`
                        resDev.innerHTML+=` Sizning javob: ${answers}`
                    }
                }
            }
            resaultBox.append(resDev)

        })
    },
    error: function(error){
        console.log(error)
    }
   })
}
function stopTextColor() {
  clearInterval(timer);
  clearTimeout(clearVaqt);

  clearVaqt=null;
  // release our intervalID from the variable
  timer = null;
}


quizForm.addEventListener('submit', e=>{
    e.preventDefault();
    // clearTimeout(clearVaqt);
    stopTextColor;
    // e.clearInterval(timer);
    sendData();
});
