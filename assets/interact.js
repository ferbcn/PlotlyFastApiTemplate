interact('#draggable')
    .draggable({
        inertia: true,
        modifiers: [
            interact.modifiers.restrictRect({
                restriction: 'parent',
                endOnly: true
            })
        ],
        autoScroll: true,
        onmove: function (event) {
            var target = event.target;
            var x = (parseFloat(target.getAttribute('data-x')) || 0) + event.dx;
            var y = (parseFloat(target.getAttribute('data-y')) || 0) + event.dy;

            target.style.webkitTransform =
            target.style.transform =
                'translate(' + x + 'px, ' + y + 'px)';

            target.setAttribute('data-x', x);
            target.setAttribute('data-y', y);
        }
    });
interact('#draggable2')
    .draggable({
        inertia: true,
        modifiers: [
            interact.modifiers.restrictRect({
                restriction: 'parent',
                endOnly: true
            })
        ],
        autoScroll: true,
        onmove: function (event) {
            var target = event.target;
            var x = (parseFloat(target.getAttribute('data-x')) || 0) + event.dx;
            var y = (parseFloat(target.getAttribute('data-y')) || 0) + event.dy;

            target.style.webkitTransform =
            target.style.transform =
                'translate(' + x + 'px, ' + y + 'px)';

            target.setAttribute('data-x', x);
            target.setAttribute('data-y', y);
        }
    });
