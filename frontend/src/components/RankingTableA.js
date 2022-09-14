import Table from 'react-bootstrap/Table';
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import './RankingTable.css'

const RankingTableA = (props) => {
    const [posts, setPosts] = useState({blogs: []});

    useEffect(() => {
        const getData = async() => {
            const {data} = await axios.get("/getRankingA")
            setPosts({blogs: data});
        };
        getData();
    }, [setPosts])

    return (
        <div> 
            <h className="header">Group 1 Results</h>
        <Table striped bordered hover>
            
            <thead>
                <tr>
                <th>Rank</th>
                <th>Team</th>
                <th>Registration Date</th>
                <th>Win</th>
                <th>Draw</th>
                <th>Lose</th>
                <th>Number of goals</th>
                <th>Score</th>
                <th>Alternate Score</th>
                </tr>
            </thead>
            <tbody>
                
                {
                    posts.blogs.map((item) => {
                        if (item[0] <= 4) {
                            return (
                                <tr key={item[0]}>
                                    <td class="p-3 mb-2 bg-success text-white">{item[0]}</td>
                                    <td class="p-3 mb-2 bg-success text-white">{item[1]}</td>
                                    <td class="p-3 mb-2 bg-success text-white">{item[2]}</td>
                                    <td class="p-3 mb-2 bg-success text-white">{item[7]}</td>
                                    <td class="p-3 mb-2 bg-success text-white">{item[9]}</td>
                                    <td class="p-3 mb-2 bg-success text-white">{item[8]}</td>
                                    <td class="p-3 mb-2 bg-success text-white">{item[6]}</td>
                                    <td class="p-3 mb-2 bg-success text-white">{item[4]}</td>
                                    <td class="p-3 mb-2 bg-success text-white">{item[5]}</td>
                                </tr>
                            )
                        }
                        else {
                            return (
                                <tr key={item[0]}>
                                    <td>{item[0]}</td>
                                    <td>{item[1]}</td>
                                    <td>{item[2]}</td>
                                    <td>{item[7]}</td>
                                    <td>{item[9]}</td>
                                    <td>{item[8]}</td>
                                    <td>{item[6]}</td>
                                    <td>{item[4]}</td>
                                    <td>{item[5]}</td>
                                </tr>
                            )
                        }
                        
                    })
                }
            </tbody>
        </Table>
        </div>
    )
}

export default RankingTableA;