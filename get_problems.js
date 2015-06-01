// get problems from leetcode

var trs = $("tr")
trs = trs.slice(2)

var problems = []
$.each(trs, function(index, item) {
    try {
        var pid = item.getElementsByTagName("td")[1].innerText
        pid = parseInt(pid)
        if (isNaN(pid)) {
            return;
        }

        var link = item.getElementsByTagName("a")[0]
        var title = link.innerText
        var href = link.href
        if (typeof title === "undefined" || typeof href === "undefined") {
            return;
        }

        problems.push({
            id: pid,
            title: title,
            href: href
        });
    } catch (e) {
        console.log(e)
    }
})

// string
console.log(JSON.stringify(problems))
