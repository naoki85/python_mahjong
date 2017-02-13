% rebase('base.tpl')

<div style="text-align: center;">
        <div>
        % for hand in my_hand:
        <div style="float: left;">
            <img src="img/{{hand}}.gif">
        </div>
        % end
    </div>
    <div style="clear: both;"></div>
    <div class="alert alert-danger">あがれる確率は{{ret_value}}%だよ！</div>
        <input class="btn btn-warning" type="button" onclick="location.href='index'" value="配牌選択に戻る" />
</div>

