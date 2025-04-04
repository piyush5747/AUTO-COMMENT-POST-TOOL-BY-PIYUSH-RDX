<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Facebook Comment Automator (Cookie Version)</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <style>
        :root {
            --primary: #4267B2;
            --secondary: #898F9C;
            --success: #4CAF50;
            --danger: #F44336;
            --light: #F5F6F7;
            --dark: #1D2129;
            --border: #DDDFE2;
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Poppins', sans-serif;
        }
        
        body {
            background-color: var(--light);
            color: var(--dark);
            line-height: 1.6;
        }
        
        .container {
            max-width: 800px;
            margin: 2rem auto;
            padding: 2rem;
            background: white;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        }
        
        h1 {
            color: var(--primary);
            text-align: center;
            margin-bottom: 1.5rem;
            font-weight: 600;
        }
        
        .form-group {
            margin-bottom: 1.5rem;
        }
        
        label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: 500;
            color: var(--dark);
        }
        
        input, textarea, select {
            width: 100%;
            padding: 0.75rem;
            border: 1px solid var(--border);
            border-radius: 5px;
            font-size: 1rem;
            transition: border 0.3s;
        }
        
        input:focus, textarea:focus, select:focus {
            outline: none;
            border-color: var(--primary);
        }
        
        textarea {
            min-height: 120px;
            resize: vertical;
        }
        
        .btn {
            display: inline-block;
            padding: 0.75rem 1.5rem;
            background-color: var(--primary);
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 1rem;
            font-weight: 500;
            transition: background 0.3s;
            text-align: center;
        }
        
        .btn:hover {
            background-color: #365899;
        }
        
        .btn-block {
            display: block;
            width: 100%;
        }
        
        .btn-success {
            background-color: var(--success);
        }
        
        .btn-success:hover {
            background-color: #3d8b40;
        }
        
        .stats {
            background-color: var(--light);
            padding: 1rem;
            border-radius: 5px;
            margin-top: 1.5rem;
            display: flex;
            justify-content: space-between;
            flex-wrap: wrap;
        }
        
        .stat-box {
            flex: 1;
            min-width: 150px;
            text-align: center;
            margin: 0.5rem;
        }
        
        .stat-box h3 {
            color: var(--primary);
            margin-bottom: 0.5rem;
            font-size: 1rem;
        }
        
        .counter {
            font-size: 1.5rem;
            font-weight: 600;
            color: var(--primary);
        }
        
        .alert {
            padding: 1rem;
            border-radius: 5px;
            margin-bottom: 1rem;
            display: none;
        }
        
        .alert-success {
            background-color: #E8F5E9;
            color: var(--success);
            border: 1px solid #C8E6C9;
        }
        
        .alert-danger {
            background-color: #FFEBEE;
            color: var(--danger);
            border: 1px solid #FFCDD2;
        }
        
        .delay-range {
            display: flex;
            gap: 1rem;
        }
        
        .delay-range > div {
            flex: 1;
        }
        
        .instructions {
            background-color: #E3F2FD;
            padding: 1rem;
            border-radius: 5px;
            margin-bottom: 1.5rem;
            font-size: 0.9rem;
        }
        
        .instructions h3 {
            color: var(--primary);
            margin-bottom: 0.5rem;
        }
        
        .instructions ol {
            padding-left: 1.2rem;
        }
        
        .instructions li {
            margin-bottom: 0.5rem;
        }
        
        .cookie-status {
            color: var(--success);
            font-weight: 500;
        }
        
        @media (max-width: 600px) {
            .delay-range {
                flex-direction: column;
            }
            
            .stat-box {
                min-width: 100%;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1><i class="fab fa-facebook"></i> Create by Piyush Facebook Comment Automator (Cookie Version)</h1>
        
        <div class="instructions">
            <h3>कैसे इस्तेमाल करें (How to Use):</h3>
            <ol>
                <li><strong>Facebook Cookies इकट्ठा करें</strong> - ब्राउज़र से 'c_user' और 'xs' कुकीज़ निकालें</li>
                <li><strong>कुकीज़ डालें</strong> - नीचे बॉक्स में हर कुकी नई लाइन पर (फॉर्मेट: c_user=123; xs=abc...)</li>
                <li><strong>पोस्ट आईडी डालें</strong> - जिस पोस्ट पर कमेंट करना है उसका आईडी</li>
                <li><strong>कमेंट्स लिस्ट बनाएं</strong> - अलग-अलग कमेंट्स (हर कमेंट नई लाइन पर)</li>
                <li><strong>सेटिंग सेव करें</strong> और "Start Commenting" बटन दबाएं</li>
                <li><strong>स्क्रिप्ट अपने आप</strong> सभी कुकीज़ को रोटेट करके कमेंट करेगी</li>
            </ol>
        </div>
        
        <div id="alert-success" class="alert alert-success"></div>
        <div id="alert-danger" class="alert alert-danger"></div>
        
        <form id="config-form">
            <div class="form-group">
                <label for="cookies">Facebook Cookies (एक कुकी प्रति लाइन)</label>
                <textarea id="cookies" name="cookies" required></textarea>
                <p id="cookie-count" class="cookie-status"></p>
            </div>
            
            <div class="form-group">
                <label for="post_id">Post ID</label>
                <input type="text" id="post_id" name="post_id" required>
            </div>
            
            <div class="form-group">
                <label for="comments">Comments (एक कमेंट प्रति लाइन)</label>
                <textarea id="comments" name="comments" required></textarea>
            </div>
            
            <div class="form-group">
                <label>Delay Between Comments (seconds)</label>
                <div class="delay-range">
                    <div>
                        <label for="delay_min">Minimum</label>
                        <input type="number" id="delay_min" name="delay_min" min="10" max="600" required>
                    </div>
                    <div>
                        <label for="delay_max">Maximum</label>
                        <input type="number" id="delay_max" name="delay_max" min="20" max="1200" required>
                    </div>
                </div>
            </div>
            
            <div class="form-group">
                <label for="max_comments">Maximum Comments Per Day</label>
                <input type="number" id="max_comments" name="max_comments" min="100" max="1500" required>
            </div>
            
            <button type="submit" class="btn">Save Configuration</button>
        </form>
        
        <div class="stats">
            <div class="stat-box">
                <h3>Today's Comment Count</h3>
                <div class="counter" id="comment-counter">0</div>
            </div>
            <div class="stat-box">
                <h3>Active Cookies</h3>
                <div class="counter" id="active-cookies">0</div>
            </div>
            <div class="stat-box">
                <h3>Total Cookies</h3>
                <div class="counter" id="total-cookies">0</div>
            </div>
        </div>
        
        <button id="start-btn" class="btn btn-success btn-block">Start Commenting</button>
    </div>
    
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script>
        $(document).ready(function() {
            // Load initial data
            $.get('/').done(function(data) {
                // This would be better with a proper API endpoint
                $('#post_id').val(data.post_id || '');
                $('#comments').val(data.comments || '');
                $('#delay_min').val(data.delay_min || 30);
                $('#delay_max').val(data.delay_max || 120);
                $('#max_comments').val(data.max_comments || 1000);
                $('#comment-counter').text(data.comment_count || 0);
                $('#cookies').val(data.cookies || '');
                $('#active-cookies').text(data.active_cookies || 0);
                $('#total-cookies').text(data.cookies ? data.cookies.split('\n').length : 0);
            });
            
            // Update cookie count display
            $('#cookies').on('input', function() {
                const count = $(this).val().split('\n').filter(line => line.trim()).length;
                $('#total-cookies').text(count);
                $('#cookie-count').text(`${count} cookies loaded`);
            });
            
            // Save config
            $('#config-form').submit(function(e) {
                e.preventDefault();
                
                $.post('/update_config', $(this).serialize())
                    .done(function(response) {
                        showAlert('success', response.message);
                    })
                    .fail(function() {
                        showAlert('danger', 'Failed to save configuration');
                    });
            });
            
            // Start commenting
            $('#start-btn').click(function() {
                $(this).prop('disabled', true).html('<i class="fas fa-spinner fa-spin"></i> Starting...');
                
                $.post('/start_commenting')
                    .done(function(response) {
                        if (response.status === 'success') {
                            showAlert('success', response.message);
                            $('#comment-counter').text(response.comment_count);
                        } else {
                            showAlert('danger', response.message);
                        }
                    })
                    .fail(function() {
                        showAlert('danger', 'An error occurred');
                    })
                    .always(function() {
                        $('#start-btn').prop('disabled', false).html('Start Commenting');
                    });
            });
            
            function showAlert(type, message) {
                const alertDiv = $(`#alert-${type}`);
                alertDiv.text(message).fadeIn();
                setTimeout(() => alertDiv.fadeOut(), 5000);
            }
        });
    </script>
</body>
</html>