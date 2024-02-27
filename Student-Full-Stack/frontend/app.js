const URL_ALL_STUDENTS = "http://127.0.0.1:5000/api/v1/students/";

/* Creates and returns an Axios client */
const getClient = (baseURL) => {
  return axios.create({
    baseURL: baseURL
  });
};

const createStudentItem = (stud) => {
  let studentContainer = document.getElementById('studentContainer')
  let li = document.createElement('li')
  li.innerText = `ID: ${stud.id} | Name: ${stud.first_name} ${stud.last_name} | Age: ${stud.age} | Subject: ${stud.subject}`
  li.addEventListener('mouseover', (event)=>{
      event.target.style.backgroundColor = 'yellow'
      event.target.style.fontSize = '30px'
  })
  li.addEventListener('mouseout',(event)=>{
      event.target.style.backgroundColor = null
      event.target.style.fontSize = null
  })
  li.addEventListener('click', (event)=>{
      event.target.style.textDecoration = 'line-through'
  })
  studentContainer.appendChild(li)
}

const addStudent = async (event) => {
  event.preventDefault()
  const data = new FormData(event.target);
  const formattedData = Object.fromEntries(data);

  console.log('here in addStudent');
  console.log(formattedData);

  /* Send post request to backend server */
  const response = await getClient(URL_ALL_STUDENTS).post(
    URL_ALL_STUDENTS,
    formattedData,
    {
      headers: {
        'Content-Type': 'application/json',
      },
    }
  );
}

const fillColor = (event, clr) => {
  event.stopPropagation()
  let elmnt = event.target
  console.log(event)
  elmnt.style.backgroundColor = clr
}

const getStudents = async() => {
  let response = await fetch(URL_ALL_STUDENTS);
  let students = await response.json();

  students.map((stud) => {
      createStudentItem(stud);
  })
}

