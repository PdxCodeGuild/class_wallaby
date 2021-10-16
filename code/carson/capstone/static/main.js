console.log('hello worl');

const navSlide = () => {
    const burger = document.querySelector('.burger')
    const nav = document.querySelector('.nav-links')
    const navLinks = document.querySelectorAll('.nav-links li');

    burger.addEventListener('click', () => {
        //Toggle NAv   
        nav.classList.toggle('nav-active');
        //Animate Links
        navLinks.forEach((link, index) => {
            if (link.style.animation) {
                link.style.animation = ''
            } else {
                link.style.animation = `navLinkFade 0.5s ease forwards ${index / 7 + 1}s `;
                console.log(index / 7)
            }
        });
        //Burger Animation
        burger.classList.toggle('toggle');

    });
}

navSlide();

document.addEventListener('DOMContentLoaded', function () {
    const calendarEl = document.getElementById('calendar');
    const calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
        themeSystem: 'bootstrap',
         eventColor: '#CF007E',
         editable:true,
         eventLimit:true,
        selectHelper:true,
        selectable: true,
        contentHeight: 600,
        customButtons: {
            myCustomButton: {
                text: 'custom!',
                click: function () {
                    alert('clicked the custom button!');
                }
            }
        },
        headerToolbar: {
            end: 'prev,next today myCustomButton',
            center: 'title',
            start: 'dayGridMonth,timeGridWeek,timeGridDay'
        },
        navLinks: true,
        navLinkWeekClick: function (weekStart, jsEvent) {
            console.log('week start', weekStart.toISOString());
            console.log('coords', jsEvent.pageX, jsEvent.pageY);
        },
        events: [
            {
                title: 'Its time',
                start: '2021-10-10T14:30:00',
                allDay: false
            }
            // other events here...
        ],
        eventTimeFormat: { // like '14:30:00'
            hour: '2-digit',
            minute: '2-digit',
            second: '2-digit',
            meridiem: false

        },
        eventDisplay: {
            display:'auto'
        },
        eventClick: function(info) {
            // alert('Event: ' + info.event.title);
            // alert('Coordinates: ' + info.jsEvent.pageX + ',' + info.jsEvent.pageY);
            // alert('View: ' + info.view.type);
        
            // change the border color just for fun
            info.el.style.borderColor = 'blue';
          },


          function( fetchInfo, successCallback, failureCallback ) {
              successCallback(eventsArr)
           }


    });

    calendar.render();

});

// (myModal).on(shown.bs.modal), function () {
//     (myInput).trigger(focus),
//   });