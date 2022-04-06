Bài test 1:

Dev cần phải viết 1 Python Decorator cho chức năng xác thực tài khoản
Id trong hệ thống sẽ sử dụng UUID thay vì một số nguyên tăng dần
Hệ thống sẽ sử dụng JWT để tạo token và xác thực (nếu không biết JWT là gì thì hỏi
Cart sau khi checkout sẽ chuyển đổi thành Order với giá trị giữ nguyên. Sau khi chuyển đổi, cart sẽ bị xoá khỏi DB
Trong order có thuộc tính payment_status: mặc định lúc checkout xong payment status sẽ là INIT
Các thao tác như cart/add, cart-item/changeQty cart-item/remove sẽ làm thay đổi cart do đó cần tính toán lại các giá trị SubTotal-Ex-Tax, Tax, Total của cart



### Create database
    brew install postgresql 
    brew install pgadmin4
    brew services start postgresql
    psql -h /tmp/ postgres
    CREATE USER admin SUPERUSER PASSWORD 'admin';
    CREATE DATABASE test_db WITH OWNER = admin;


### Terminal commands
Note: make sure you have `pip` and `virtualenv` installed.

 - activate 'vitualenv' 
    python3 -m venv env
    . env/bin/activate

 - after activate virtualenv, install requirements.txt
    pip install -r requirements.txt

    
Make sure to run the initial migration commands to update the database.
    
    > flask db init

    > flask db migrate

    > flask db upgrade

### Viewing the app ###
    flask run
    Open the following url on your browser to view swagger documentation
    http://127.0.0.1:5000/


