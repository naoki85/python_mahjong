% rebase('base.tpl')
<style>
button {
    background-color: transparent;
    border: none;
}
</style>
<script>
$(function() {
    var selected_count = 0;
    $('.tile').on('click', function() {
        selected_count += 1;
        if (selected_count > 13) {
            alert('選択できるのは13枚までです。1度リセットしてください。');
            return;
        }
        tile = $(this).val();
        html_input = '<input name="tile" type="hidden" value="' + tile + '" />';
        html_img = '<img src="img/' + tile + '.gif">';
        $('form').prepend(html_input);
        $('form').prepend(html_img);
    });
});
</script>
<div style="text-align: center; max-width: 100%;">
    <div class="well well-lg" style="text-align: left;">
        配牌の13牌を選んでね！
    </div>
    <div>
        % characters = [11,12,13,14,15,16,17,18,19]
        % for char in characters:
        <div style="float: left;">
            <button class="tile" value="{{char}}">
                <img src="img/{{char}}.gif">
            </button>
        </div>
        % end
    </div>
    <div style="clear: both;"></div>
        <div>
        % circles = [21,22,23,24,25,26,27,28,29]
        % for circle in circles:
        <div style="float: left;">
            <button class="tile" value="{{circle}}">
                <img src="img/{{circle}}.gif">
            </button>
        </div>
        % end
    </div>
    <div style="clear: both;"></div>
        <div>
        % bamboos = [31,32,33,34,35,36,37,38,39]
        % for bamboo in bamboos:
        <div style="float: left;">
            <button class="tile" value="{{bamboo}}">
                <img src="img/{{bamboo}}.gif">
            </button>
        </div>
        % end
    </div>
    <div style="clear: both;"></div>
        <div>
        % honours = [41,42,43,44,45,46,47]
        % for honour in honours:
        <div style="float: left;">
            <button class="tile" value="{{honour}}">
                <img src="img/{{honour}}.gif">
            </button>
        </div>
        % end
    </div>
    <div style="clear: both;"></div>
    <hr>
    <form action="show_result" method="get">
        <br />
        <input class="btn btn-info" type="submit" value="結果は？" />
        <input class="btn btn-warning" type="button" onclick="location.href='index'" value="リセット" />
    </form>
</div>
