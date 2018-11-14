# Verify that the service is running.
describe http('https://localhost/users/login', 
              ssl_verify: false,
              enable_remote_worker: true) do
  its('status') { should eq 200 }
end

describe file('/etc/foreman-installer/scenarios.d/foreman-answers.yaml') do
  it { should exist }  
end

describe service('httpd') do
  it { should be_running }  
end

describe service('foreman-proxy') do
  it { should be_running }  
end

describe port(3306) do
  it { should be_listening }
  its('processes') {should include 'mysqld'}
  its('addresses') {should include '127.0.0.1'}
end



